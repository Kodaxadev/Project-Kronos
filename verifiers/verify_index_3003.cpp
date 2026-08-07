#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <tuple>
#include <vector>

using u64 = std::uint64_t;

static constexpr u64 ELL = 3003;
static constexpr u64 LOWER = (u64{1} << 30);
static constexpr u64 UPPER = 2304192002ULL;

u64 mod_pow(u64 base, u64 exponent, u64 modulus) {
    u64 result = 1;
    while (exponent) {
        if (exponent & 1U) result = (result * base) % modulus;
        base = (base * base) % modulus;
        exponent >>= 1U;
    }
    return result;
}

std::vector<int> sieve_primes(int limit) {
    std::vector<bool> prime(limit + 1, true);
    if (limit >= 0) prime[0] = false;
    if (limit >= 1) prime[1] = false;
    for (int p = 2; p * p <= limit; ++p) {
        if (!prime[p]) continue;
        for (int multiple = p * p; multiple <= limit; multiple += p) prime[multiple] = false;
    }
    std::vector<int> out;
    for (int p = 2; p <= limit; ++p) if (prime[p]) out.push_back(p);
    return out;
}

u64 inverse_mod(u64 a, u64 modulus) {
    std::int64_t t = 0, new_t = 1;
    std::int64_t r = static_cast<std::int64_t>(modulus);
    std::int64_t new_r = static_cast<std::int64_t>(a % modulus);
    while (new_r != 0) {
        std::int64_t q = r / new_r;
        std::tie(t, new_t) = std::make_tuple(new_t, t - q * new_t);
        std::tie(r, new_r) = std::make_tuple(new_r, r - q * new_r);
    }
    if (r != 1) throw std::runtime_error("inverse does not exist");
    if (t < 0) t += static_cast<std::int64_t>(modulus);
    return static_cast<u64>(t);
}

std::vector<u64> progression_primes(u64 lower, u64 upper, u64 step, u64& first_k, u64& last_k) {
    first_k = lower / step + 1;
    last_k = (upper - 1) / step;
    const std::size_t size = static_cast<std::size_t>(last_k - first_k + 1);
    std::vector<std::uint8_t> composite(size, 0);
    auto primes = sieve_primes(static_cast<int>(std::sqrt(static_cast<long double>(upper - 1))));
    for (int q_int : primes) {
        const u64 q = static_cast<u64>(q_int);
        if (step % q == 0) continue;
        const u64 residue = (q - inverse_mod(step, q)) % q;
        u64 start = residue;
        if (start < first_k) start += ((first_k - start + q - 1) / q) * q;
        for (u64 k = start; k <= last_k; k += q) composite[static_cast<std::size_t>(k - first_k)] = 1;
    }
    std::vector<u64> out;
    for (u64 k = first_k; k <= last_k; ++k) {
        if (!composite[static_cast<std::size_t>(k - first_k)]) out.push_back(step * k + 1);
    }
    return out;
}

std::vector<u64> distinct_factors(u64 n, const std::vector<int>& primes) {
    std::vector<u64> out;
    for (int q_int : primes) {
        const u64 q = static_cast<u64>(q_int);
        if (q * q > n) break;
        if (n % q == 0) {
            out.push_back(q);
            while (n % q == 0) n /= q;
        }
    }
    if (n > 1) out.push_back(n);
    return out;
}

bool exact_order(u64 a, u64 order, u64 p, const std::vector<u64>& factors) {
    if (mod_pow(a, order, p) != 1) return false;
    for (u64 q : factors) if (mod_pow(a, order / q, p) == 1) return false;
    return true;
}

bool target_index(u64 p, const std::vector<int>& primes, u64& subgroup_size, u64& order_two) {
    subgroup_size = (p - 1) / ELL;
    if (subgroup_size % 2 != 0) return false;
    auto factors_h = distinct_factors(subgroup_size, primes);
    if (exact_order(2, subgroup_size, p, factors_h)) {
        order_two = subgroup_size;
        return true;
    }
    const u64 half = subgroup_size / 2;
    if (half % 2 == 1 && exact_order(2, half, p, distinct_factors(half, primes))) {
        order_two = half;
        return true;
    }
    return false;
}

u64 primitive_root(u64 p, const std::vector<u64>& factors) {
    for (u64 g = 2; g < p; ++g) {
        bool ok = true;
        for (u64 q : factors) {
            if (mod_pow(g, (p - 1) / q, p) == 1) { ok = false; break; }
        }
        if (ok) return g;
    }
    throw std::runtime_error("primitive root not found");
}

struct Record { u64 p, h, order2, g, b, c, exponent; };

Record witness(u64 p, u64 h, u64 order2, const std::vector<int>& primes) {
    const auto factors = distinct_factors(p - 1, primes);
    const u64 g = primitive_root(p, factors);
    const u64 step = mod_pow(g, ELL, p);
    const u64 target = mod_pow(g, 2 * h, p);
    u64 element = 1;
    for (u64 exponent = 0; exponent < h; ++exponent) {
        const u64 b = (g * element) % p;
        const u64 c = (b + 1) % p;
        if (c != 0 && mod_pow(c, h, p) == target) return {p, h, order2, g, b, c, exponent};
        element = (element * step) % p;
    }
    throw std::runtime_error("witness not found");
}

int main() {
    const u64 step = 2 * ELL;
    u64 first_k = 0, last_k = 0;
    auto primes = progression_primes(LOWER, UPPER, step, first_k, last_k);
    auto trial_primes = sieve_primes(static_cast<int>(std::sqrt(static_cast<long double>(UPPER - 1))));
    std::vector<Record> records;
    for (u64 p : primes) {
        u64 h = 0, order2 = 0;
        if (target_index(p, trial_primes, h, order2)) records.push_back(witness(p, h, order2, trial_primes));
    }
    std::cout << "ELL " << ELL << "\n";
    std::cout << "LOWER_EXCLUSIVE " << LOWER << "\n";
    std::cout << "UPPER_EXCLUSIVE " << UPPER << "\n";
    std::cout << "FIRST_K " << first_k << "\n";
    std::cout << "LAST_K " << last_k << "\n";
    std::cout << "PROGRESSION_CANDIDATES " << (last_k - first_k + 1) << "\n";
    std::cout << "PRIME_CANDIDATES " << primes.size() << "\n";
    std::cout << "INDEXED_PRIMES " << records.size() << "\n";
    for (const auto& r : records) {
        std::cout << "P " << r.p << " H " << r.h << " ORD2 " << r.order2
                  << " G " << r.g << " B " << r.b << " C " << r.c
                  << " EXP " << r.exponent << "\n";
    }
    return 0;
}
