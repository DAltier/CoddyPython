def organize_contacts(contact_list):
    # Your solution here
    
    # 1. Create helper functions for validation
    # - Function to validate email format
    # - Function to clean and validate phone numbers
    
    # 2. Process each contact
    # - Clean email (lowercase) and phone (digits only)
    # - Check if email and phone are valid
    # - Check for duplicates
    
    # 3. Return the clean contact list
    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()

    def is_valid_email(email):
        return "@" in email and "." in email and " " not in email

    def clean_and_validate_phone(phone):
        cleaned = ''.join(ch for ch in phone if ch.isdigit())
        return cleaned if len(cleaned) == 10 else None

    for contact in contact_list:
        name = contact.get("name", "").strip()
        email = contact.get("email", "").strip().lower()
        phone_raw = contact.get("phone", "")
        phone = clean_and_validate_phone(phone_raw)

        if not is_valid_email(email) or not phone:
            continue

        if email in seen_emails or phone in seen_phones:
            continue

        cleaned_contacts.append({
            "name": name,
            "email": email,
            "phone": phone
        })

        seen_emails.add(email)
        seen_phones.add(phone)
    
    return cleaned_contacts