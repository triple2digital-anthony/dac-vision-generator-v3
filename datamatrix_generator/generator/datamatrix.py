"""
DataMatrix Code Generator for Blue, Black & Red Caps

This module implements the core code generation algorithm that matches the patterns
identified in the cap datasets, using the appropriate prefixes for each type.
"""

from typing import List, Dict, Set, Tuple, Optional
import random
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """Result of code validation."""
    valid: bool
    reason: Optional[str] = None
    cap_color: Optional[str] = None

class DataMatrixCodeGenerator:
    """Python implementation of the DataMatrix Code Generator with identical functionality to the JavaScript version."""
    
    def __init__(self):
        # Character set (Base32-like encoding)
        self.charset = "23456789abcdefghijkmnpqrstuvwxyz"
        
        # Mapping tables
        self.char_to_value = {char: i for i, char in enumerate(self.charset)}
        self.value_to_char = {i: char for i, char in enumerate(self.charset)}
        
        # Even digits for the last character (checksum)
        self.even_digits = ["2", "4", "6", "8"]
        
        # Common prefixes observed in all datasets
        self.blue_prefixes = [
            # Starting with 6
            "65e", "65f", "65g", "65h", "688", "689", "683", "686", "687", 
            "644", "646", "647", "648", "649",
            # Starting with 7
            "736", "737", "738", "739", "767", "768", "77f", "77g", "77h", 
            "72c", "72f", "72g", "72h", "7pb", "7pc", "7pd", "7pg", "7z7",
            "7m5", "7v8", "7ua", "7kf", "7hn", "7hr", "7ya", "7yb", "7yc", 
            # Starting with v
            "vxp", "vxq", "vxr", "viv", "viw", "vjm", "vjq", "vwx", "vww", 
            "vn2", "vn6", "vn7", "vn8", "vn9", "vcw", "vcx", "vcz", "vdn"
        ]
        
        self.black_prefixes = [
            # Starting with 6
            "647", "649", "65e", "65g", "686", "689",
            # Starting with 7
            "736", "739", "767", "768", "77a", "77f", "77g",
            "72c", "7c3", "7c8", "7c9", "7de", "7df", "7dg", "7dh", "7gw",
            "7gx", "7gy", "7gz", "7hp", "7hr", "7kb", "7kc", "7kd", "7kf",
            "7m5", "7n2", "7pa", "7pc", "7pd", "7ud", "7ua", "7uc", "7v4",
            # Starting with v
            "vcy", "vdn", "vdr", "vn6", "vn7", "vn8", "vn9", "vpe", "vpf", 
            "vpg", "vph", "vs6", "vs7", "vtb", "vtg", "vww", "vwy", "vwz",
            "vxp", "vxq", "vxr", "viw", "vjm", "vju", "vcu", "vcw"
        ]
        
        self.red_prefixes = [
            # Starting with 6
            "646", "647", "649", "65e", "65h", "683", "687", "688",
            # Starting with 7
            "72e", "72f", "72g", "72h", "736", "737", "738", "739", "768", "77g", "77h",
            "7c3", "7c6", "7c7", "7c9", "7de", "7dh", "7gx", "7gz", "7hm", "7hn", "7hp",
            "7hq", "7hr", "7ka", "7kb", "7kc", "7kf", "7m5", "7n2", "7n5", "7pa", "7pb",
            "7pg", "7ua", "7uc", "7ud", "7v3", "7v4", "7v5", "7v8", "7ya", "7yc", "7yd",
            "7z2", "7z3", "7z4", "7z5",
            # Starting with v
            "v8n", "v8p", "v9w", "v9x", "v9y", "v9z", "vcx", "vcy", "vcz", "vdn", "vdq",
            "vis", "viu", "vji", "vjj", "vjk", "vn6", "vn8", "vn9", "vpf", "vpg", "vph",
            "vs6", "vs8", "vs9", "vtb", "vte", "vtf", "vtg", "vww", "vwx", "vwy", "vwz", "vxp"
        ]
        
        # Combined prefixes with duplicates removed
        self.combined_prefixes = list(set(self.blue_prefixes + self.black_prefixes + self.red_prefixes))
        
        # Current active prefixes
        self.active_prefixes = self.blue_prefixes
        
        # First character distribution
        self.first_char_dist = {
            "7": 50.0,
            "v": 37.8,
            "6": 12.2
        }
        
        # Current cap type
        self.cap_type = "blue"
    
    def set_cap_type(self, type: str) -> None:
        """Set the active cap type (blue, black, red, or all)."""
        self.cap_type = type
        
        if type == "blue":
            self.active_prefixes = self.blue_prefixes
        elif type == "black":
            self.active_prefixes = self.black_prefixes
        elif type == "red":
            self.active_prefixes = self.red_prefixes
        elif type == "all":
            self.active_prefixes = self.combined_prefixes
        else:
            self.active_prefixes = self.blue_prefixes
    
    def value_to_binary(self, value: int) -> str:
        """Convert a value to its 5-bit binary representation."""
        return format(value & 0x1F, '05b')
    
    def binary_to_char(self, binary: str) -> str:
        """Convert a binary string to its Base32 character."""
        value = int(binary, 2)
        return self.value_to_char.get(value, self.value_to_char[0])
    
    def calculate_checksum(self, code: str) -> int:
        """Calculate checksum for a code using XOR of values modulo 4."""
        sum_xor = 0
        for char in code:
            value = self.char_to_value.get(char, 0)
            sum_xor ^= value
        return sum_xor % 4
    
    def checksum_to_even_digit(self, checksum_value: int) -> str:
        """Map a checksum value (0-3) to an even digit (2,4,6,8)."""
        return self.even_digits[checksum_value]
    
    def weighted_choice(self, choices: Dict[str, float]) -> str:
        """Weighted choice from a distribution object."""
        total = sum(choices.values())
        r = random.uniform(0, total)
        cumulative = 0
        
        for item, weight in choices.items():
            cumulative += weight
            if r <= cumulative:
                return item
        return list(choices.keys())[0]  # Fallback
    
    def generate_random_code(self) -> str:
        """Generate a random code that follows the identified pattern."""
        # Step 1: Choose a prefix
        if random.random() < 0.8:  # 80% chance to use common prefix
            prefix = random.choice(self.active_prefixes)
        else:
            # Generate a new prefix with proper first character distribution
            first_char = self.weighted_choice(self.first_char_dist)
            rest_length = 2 + random.randint(0, 1)  # 2-3 more chars
            rest_chars = ''.join(random.choice(self.charset) for _ in range(rest_length))
            prefix = first_char + rest_chars
        
        # Step 2: Generate the middle section
        middle_length = 25 - len(prefix)
        middle_chars = ''
        
        for _ in range(middle_length):
            if random.random() < 0.25:  # 25% chance for digit
                middle_chars += random.choice(self.charset[:8])  # Digits only
            else:
                middle_chars += random.choice(self.charset[8:])  # Letters only
        
        # Step 3: Combine prefix and middle to form the data part
        data_section = prefix + middle_chars
        
        # Step 4: Calculate the checksum
        checksum_value = self.calculate_checksum(data_section)
        checksum_digit = self.checksum_to_even_digit(checksum_value)
        
        # Step 5: Return the complete code
        return data_section + checksum_digit
    
    def generate_sequential_code(self, counter_value: int, prefix_type: str = "7") -> str:
        """Generate a code with a specific counter value embedded."""
        # Step 1: Choose a prefix based on the prefixType
        matching_prefixes = [p for p in self.active_prefixes if p.startswith(prefix_type)]
        if not matching_prefixes:
            # Fallback if no matching prefixes
            first_char = prefix_type
            rest_chars = self.charset[:2]
            return self.generate_code_with_prefix(first_char + rest_chars, counter_value)
        
        prefix = matching_prefixes[counter_value % len(matching_prefixes)]
        return self.generate_code_with_prefix(prefix, counter_value)
    
    def generate_code_with_prefix(self, prefix: str, counter_value: int) -> str:
        """Generate a code with a specific prefix and counter value."""
        # Step 1: Convert counter to binary
        counter_binary = format(counter_value, '020b')
        
        # Step 2: Generate random bits for remaining positions
        remaining_bits = 25 * 5 - len(prefix) * 5 - len(counter_binary)
        random_bits = ''.join(str(random.randint(0, 1)) for _ in range(remaining_bits))
        
        # Step 3: Combine all binary data
        prefix_binary = ''.join(self.value_to_binary(self.char_to_value.get(c, 0)) for c in prefix)
        data_binary = prefix_binary + counter_binary + random_bits
        
        # Step 4: Convert binary data back to characters
        data_section = ''
        for i in range(0, len(data_binary), 5):
            chunk = data_binary[i:i+5]
            value = int(chunk, 2)
            data_section += self.value_to_char.get(value, self.value_to_char[0])
        
        # Ensure we have exactly 25 characters
        data_section = data_section[:25]
        
        # Step 5: Calculate the checksum
        checksum_value = self.calculate_checksum(data_section)
        checksum_digit = self.checksum_to_even_digit(checksum_value)
        
        # Step 6: Return the complete code
        return data_section + checksum_digit
    
    def generate_random_batch(self, count: int) -> List[str]:
        """Generate a batch of random codes."""
        codes = set()
        while len(codes) < count:
            codes.add(self.generate_random_code())
        return list(codes)
    
    def generate_sequential_batch(self, start_counter: int, count: int, prefix_type: str = "7") -> List[str]:
        """Generate a batch of sequential codes."""
        return [self.generate_sequential_code(start_counter + i, prefix_type) for i in range(count)]
    
    def determine_cap_color(self, code: str) -> str:
        """Determine the cap color based on the code prefix."""
        if not code or len(code) < 3:
            return "unknown"
        
        prefix = code[:3]
        
        # Check if prefix is unique to a specific cap color
        in_blue = prefix in self.blue_prefixes
        in_black = prefix in self.black_prefixes
        in_red = prefix in self.red_prefixes
        
        # Count how many cap types this prefix appears in
        cap_count = sum([in_blue, in_black, in_red])
        
        if cap_count == 0:
            # If prefix not found in any list, try to guess based on first character
            first_char = code[0]
            if first_char in ['6', '7', 'v']:
                return "unknown (valid format)"
            return "unknown"
        elif cap_count == 1:
            # Unique to one cap type
            if in_blue:
                return "blue"
            if in_black:
                return "black"
            if in_red:
                return "red"
        else:
            # Appears in multiple cap types
            types = []
            if in_blue:
                types.append("blue")
            if in_black:
                types.append("black")
            if in_red:
                types.append("red")
            return " or ".join(types)
        
        return "unknown"
    
    def validate_code(self, code: str) -> ValidationResult:
        """Validate if a code follows the expected pattern."""
        if not code or len(code) != 26:
            return ValidationResult(False, "Code must be 26 characters", "unknown")
        
        # Check if all characters are in the allowed charset
        for i, char in enumerate(code):
            if char not in self.charset:
                return ValidationResult(False, f"Invalid character '{char}' at position {i}", "unknown")
        
        # Check if the first character is valid
        first_char = code[0]
        if first_char not in ['6', '7', 'v']:
            return ValidationResult(False, "First character must be '6', '7', or 'v'", "unknown")
        
        # Check if last character is an even digit
        last_char = code[-1]
        if last_char not in self.even_digits:
            return ValidationResult(False, "Last character must be an even digit (2,4,6,8)", "unknown")
        
        # Check if checksum is correct
        data_section = code[:-1]
        expected_checksum = self.calculate_checksum(data_section)
        expected_digit = self.checksum_to_even_digit(expected_checksum)
        
        if last_char != expected_digit:
            return ValidationResult(
                False,
                f"Checksum is incorrect. Expected '{expected_digit}', got '{last_char}'",
                "unknown"
            )
        
        # Determine cap color
        cap_color = self.determine_cap_color(code)
        
        return ValidationResult(True, None, cap_color) 