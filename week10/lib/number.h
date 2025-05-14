#pragma once
#include <cinttypes>
#include <iostream>
#include <array>
#include <string>
#include <algorithm>
#include <stdexcept>

struct uint2022_t {
    static constexpr size_t kBits = 2022;
    static constexpr size_t kBitsPerPart = 32;
    static constexpr size_t kPartCount = (kBits + kBitsPerPart - 1) / kBitsPerPart;

    std::array<uint32_t, kPartCount> parts = { 0 };

    uint2022_t() = default;
};

static_assert(sizeof(uint2022_t) <= 300, "Size of uint2022_t must be no higher than 300 bytes");

uint2022_t from_uint(uint32_t i);
uint2022_t from_string(const char* buff);

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator<(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator>(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator<=(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator>=(const uint2022_t& lhs, const uint2022_t& rhs);

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value);