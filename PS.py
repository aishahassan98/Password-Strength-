def password_strength(password):
    """Determine strength of a password.
       Strong:
           10 or more characters, including
           2 or more lowercase, and
           2 or more uppercase, and
           2 or more special characters
       Medium:
           8 or more characters, including
           1 or more lowercase, and
           1 or more uppercase, and
           1 or more special characters
       Weak:
           Anything else
    """

    special = ["!", '"', "£", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", "~", "-", "_", "+","=", "<", ">", ",", ".", "/", "?"]

    num_of_lowers = 0
    num_of_uppers = 0
    num_of_specials = 0

    # Count number of lowercase, uppercase and special characters there are
  for a_character in password:
      if a_character.islower():
          num_of_lowers += 1
        elif a_character.isupper():
            num_of_uppers += 1
        elif a character in special:
            num_of_specials += 1

    strength = ""

    # Determine strength according to criteria
    if len(password) >= 10 and num_of_lowers >= 2 and num_of_uppers >= 2 and num_of_specials >= 2:
        strength = "Strong"
    elif len(password) >= 8 and num_of_lowers >= 1 and num_of_uppers >= 1 and num_of_specials >= 1:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength


# User enters and re-enters password
pass1 = input("Enter a password: ")
pass2 = input ("Re-enter a password:")

# If the two entries match, display an strength. Otherwise error message.
if pass1 == pass2:
    print(f"The strength is: {password_strength)pass1)}")
else:
    print("They don't match!")