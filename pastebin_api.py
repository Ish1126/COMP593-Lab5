import requests

def create_paste(title, body, expire_date, is_public):
    """
    Creates a new paste on PasteBin.

    Args:
        title (str): Title of the paste.
        body (str): Body text of the paste.
        expire_date (str): Expiration date of the paste (e.g., '1M' for 1 month).
        is_public (bool): Whether the paste should be publicly listed.

    Returns:
        str: URL of the newly created paste if successful, otherwise None.
    """
    # PasteBin API endpoint
    api_url = 'https://pastebin.com/api/api_post.php'

    # PasteBin API developer key (replace with your actual API key)
    api_dev_key = '7bWC2EY6gOvHIEry3l4YT4oQj3QkLq-4'

    # Data to be sent in the POST request
    data = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_name': title,
        'api_paste_code': body,
        'api_paste_expire_date': expire_date,
        'api_paste_private': '0' if is_public else '1'  # 0 for public, 1 for private
    }

    # Send POST request to PasteBin API
    response = requests.post(api_url, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the paste URL from the response
        paste_url = response.text.strip()
        print("New PasteBin paste created:", paste_url)
        return paste_url
    else:
        # Print error message if request failed
        print("Failed to create paste:", response.text)
        return None

# Test the function
if __name__ == "__main__":
    # Example usage
    title = "Test Paste"
    body = "This is a test paste created using the PasteBin API."
    expire_date = "1D"  # Expires after 1 day
    is_public = True  # Publicly listed
    create_paste(title, body, expire_date, is_public)
