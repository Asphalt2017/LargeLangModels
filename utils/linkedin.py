import requests
import os


def scrape_linkedin_profile(url : str, *, mock : bool = False) -> dict:
    """Scrapes a LinkedIn profile and returns the data. 

    Args:
        url (str): The LinkedIn profile URL to scrape. 
        mock (bool): If True, the function will return a mock response.

    Returns:
        dict: The scraped LinkedIn profile data.
    """

    print(f"Scraping LinkedIn profile: {url}")
    if mock :
        data = requests.get(url, timeout=10).json()

    else:
        api_key = os.environ.get('PROXYCURL_API_KEY')
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            #'twitter_profile_url': 'https://x.com/RoudraSaha',
            #'facebook_profile_url': 'https://www.facebook.com/roudra.saha.5',
            'linkedin_profile_url': url,
            'extra': 'include',
            'github_profile_id': 'include',
            'facebook_profile_id': 'include',
            'twitter_profile_id': 'include',
            'personal_contact_number': 'include',
            'personal_email': 'include',        
            'inferred_salary': 'include',
            'skills': 'include',
            'use_cache': 'if-present',
            'fallback_to_cache': 'on-error',
        }   

        response = requests.get(
            api_endpoint,
            params=params,
            headers=headers
        )

        data = response.json()

    data = { 
        k:v for k,v in data.items() 
        if v not in [None, [], ""] 
        and k not in [
            'profile_pic_url',
            'background_cover_image_url',
            'people_also_viewed', 
            'certifications', 
            #'education', 
            #'experience', 
            'interests', 
            #'languages',
            #'organizations', 
            #'patents', 
            #'projects', 
            #'publications', 
            'recommendations', 
            #'skills', 
            #'volunteering',
            'websites', 
            #'awards', 
            #'courses',
            'activities',
            'groups'  ,
            'inferred_salary'
                        ]
    }
        
    return data

