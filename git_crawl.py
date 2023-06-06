from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

def branch_top_repositories(num_repos):
    # Load credentials from cred.yaml
    with open("cred_git.yaml", "r") as file:
        credentials = yaml.safe_load(file)
    
    username = credentials["email"]
    password = credentials["password"]

    # Set up Selenium options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Set up Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    # full screen
    driver.maximize_window()

    # Navigate to GitHub
    driver.get("https://github.com")

    # wait
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
    # Find and click the "Sign in" button
    sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_link.click()

    # wait 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_field")))
    # Find and enter the username field
    username_field = driver.find_element(By.ID, "login_field")
    username_field.send_keys(username)

    # Find and enter the password field
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # Find and click the "Sign in" button
    sign_in_button = driver.find_element(By.NAME, "commit")
    sign_in_button.click()

    # Wait for the login process to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))

    # Navigate to the Explore page
    driver.get("https://github.com/krzjoa/awesome-python-data-science")

    # Wait for the trending repositories to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Box-row")))

    # Find all the links in page that have rel="noopener noreferrer"
    repositories = driver.find_elements(By.XPATH, "//a[@rel='noopener noreferrer']")

    # Get the names and URLs of the most starred repositories
    most_starred_repos = []
    for repo in repositories:
        name = repo.text.strip()
        url = repo.get_attribute("href")
        # if url has victorcouste in it or no github, skip it
        if "krzjoa" in url or "github.com" not in url:
            continue
        # go to url
        driver.get(url)
        # wait for page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pagehead-actions")))
        try:
            # get id="repo-stars-counter-star"
            stars_element = driver.find_element(By.ID, "repo-stars-counter-star")
            stars = stars_element.text.strip()
            # if k convert to *1000
            if "k" in stars:
                stars = float(stars.replace("k", "")) * 1000
            else:
                stars = int(stars)
            most_starred_repos.append((name, url, stars))
        except:
            print(f"Skipping {name} because it has no stars")

    # Sort the repositories by the number of stars (in descending order)
    most_starred_repos.sort(key=lambda x: x[2], reverse=True)

    # Branch the specified number of repositories
    for i, repo in enumerate(most_starred_repos[:num_repos]):
        name, url, stars = repo
        print(f"{i+1}. {name} - {stars} stars")
        print(f"   URL: {url}")
        # Perform the branching logic here
        # ...

    # Close the Chrome driver
    driver.quit()

# Example usage
num_repos_to_branch = 5
branch_top_repositories(num_repos_to_branch)
