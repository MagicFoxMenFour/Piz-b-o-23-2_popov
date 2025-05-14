#include "number.h"
#include <string>
#include <algorithm>
#include <stdexcept>

using namespace std;

uint2022_t from_uint(uint32_t i) {
    uint2022_t result;
    result.parts[0] = i;
    return result;
}

uint2022_t from_string(const char* buff) {
    uint2022_t result;
    string s(buff);

    // Удаляем ведущие нули
    s.erase(0, s.find_first_not_of('0'));
    if (s.empty()) {
        return result; // "0"
    }

    for (char c : s) {
        if (c < '0' || c > '9') {
            throw invalid_argument("Invalid character in number string");
        }
    }

    for (char c : s) {
        // Умножаем на 10
        uint32_t carry = 0;
        for (size_t j = 0; j < result.kPartCount; ++j) {
            uint64_t product = (uint64_t)result.parts[j] * 10 + carry;
            result.parts[j] = static_cast<uint32_t>(product);
            carry = static_cast<uint32_t>(product >> 32);
        }

        // Добавляем текущую цифру
        carry = c - '0';
        for (size_t j = 0; j < result.kPartCount && carry > 0; ++j) {
            uint64_t sum = (uint64_t)result.parts[j] + carry;
            result.parts[j] = static_cast<uint32_t>(sum);
            carry = static_cast<uint32_t>(sum >> 32);
        }
    }

    return result;
}

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint32_t carry = 0;

    for (size_t i = 0; i < result.kPartCount; ++i) {
        uint64_t sum = (uint64_t)lhs.parts[i] + rhs.parts[i] + carry;
        result.parts[i] = static_cast<uint32_t>(sum);
        carry = static_cast<uint32_t>(sum >> 32);
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint32_t borrow = 0;

    for (size_t i = 0; i < result.kPartCount; ++i) {
        uint64_t diff = (uint64_t)lhs.parts[i] - rhs.parts[i] - borrow;
        result.parts[i] = static_cast<uint32_t>(diff);
        borrow = (diff > (uint64_t)lhs.parts[i]) ? 1 : 0;
    }

    return result;
}

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;

    for (size_t i = 0; i < lhs.kPartCount; ++i) {
        uint32_t carry = 0;
        for (size_t j = 0; j < rhs.kPartCount; ++j) {
            if (i + j >= result.kPartCount) continue;

            uint64_t product = (uint64_t)lhs.parts[i] * rhs.parts[j] + result.parts[i + j] + carry;
            result.parts[i + j] = static_cast<uint32_t>(product);
            carry = static_cast<uint32_t>(product >> 32);
        }
    }

    return result;
}

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (size_t i = 0; i < lhs.kPartCount; ++i) {
        if (lhs.parts[i] != rhs.parts[i]) {
            return false;
        }
    }
    return true;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = lhs.kPartCount - 1; i >= 0; --i) {
        if (lhs.parts[i] < rhs.parts[i]) return true;
        if (lhs.parts[i] > rhs.parts[i]) return false;
    }
    return false;
}

bool operator>(const uint2022_t& lhs, const uint2022_t& rhs) {
    return rhs < lhs;
}

bool operator<=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(rhs < lhs);
}

bool operator>=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs < rhs);
}

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    if (value == uint2022_t()) {
        stream << "0";
        return stream;
    }

    uint2022_t temp = value;
    string result;

    while (temp != uint2022_t()) {
        uint32_t remainder = 0;
        for (int i = temp.kPartCount - 1; i >= 0; --i) {
            uint64_t value = ((uint64_t)remainder << 32) + temp.parts[i];
            temp.parts[i] = static_cast<uint32_t>(value / 10);
            remainder = static_cast<uint32_t>(value % 10);
        }
        result.push_back('0' + remainder);
    }

    reverse(result.begin(), result.end());
    stream << result;
    return stream;
}

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == uint2022_t()) {
        throw runtime_error("Division by zero");
    }

    if (lhs < rhs) {
        return uint2022_t();
    }

    uint2022_t quotient;
    uint2022_t current = lhs;

    while (current >= rhs) {
        current = current - rhs;
        quotient = quotient + from_uint(1);
    }

    return quotient;
}