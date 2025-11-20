import os
import requests

# Only load dotenv when running locally (not in CI/workflows)
if not os.environ.get('CI') and not os.environ.get('GITHUB_ACTIONS'):
    from dotenv import load_dotenv
    load_dotenv()

honorifics = [
    "The Immortal Lord of Heaven and Earth for Blessings",
    "The Sky Lord of Heaven and Earth for Blessings",
    "The Exalted Thearch of Heaven and Earth for Blessings",
    "The Celestial Worthy of Heaven and Earth for Blessings"
]

def get_current_bio(token):
    """Get the current user bio from GitHub"""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get("https://api.github.com/user", headers=headers)
    response.raise_for_status()
    return response.json().get("bio", "")

def update_bio(token, new_bio):
    """Update the user bio on GitHub"""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"bio": new_bio}
    response = requests.patch("https://api.github.com/user", headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def get_next_bio(current_bio):
    """Determine the next honorific based on the current bio"""
    current_honorific = None
    for h in honorifics:
        if h in current_bio:
            current_honorific = h
            break

    if current_honorific:
        index = honorifics.index(current_honorific)
        return honorifics[(index + 1) % len(honorifics)]
    else:
        return honorifics[0]

def main():
    token = os.environ.get("BIO_TOKEN")
    if not token:
        print("Error: BIO_TOKEN environment variable not set")
        return

    try:
        # Get current bio
        current_bio = get_current_bio(token)
        print(f"Current bio: {current_bio}")

        # Find which honorific is currently in the bio
        next_bio = get_next_bio(current_bio)

        print(f"Next honorific: {next_bio}")

        # Update bio with new honorific
        result = update_bio(token, next_bio)
        print(f"Bio updated successfully: {result.get('bio')}")

    except requests.exceptions.RequestException as e:
        print(f"Error updating bio: {e}")

if __name__ == "__main__":
    main()
