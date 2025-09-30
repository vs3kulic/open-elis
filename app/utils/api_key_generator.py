"""This module provides functionality to generate secure API keys."""

import secrets

def generate_api_key():
    """
    Generates a secure, URL-safe API key.
    
    :params: None
    :return: A unique API key with a prefix.
    :rtype: str
    """
    random_part = secrets.token_urlsafe(24)
    api_key = f"elis_{random_part}"

    return api_key

def main():
    """Main function to demonstrate API key generation."""
    new_key = generate_api_key()
    print(f"Generated API Key: {new_key}")

if __name__ == "__main__":
    main()
