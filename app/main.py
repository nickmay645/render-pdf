import uvicorn
from fastapi import FastAPI
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from mangum import Mangum

# Initialize FastAPI app
app = FastAPI()

# Initialize handler for AWS Lambda integration via Mangum 
handler = Mangum(app)

@app.get("/")
def root():
    return {"Hello": "World! This is a test."}


@app.get("/render")
def render(url: str, proxy_url: str):

    # Set selenium wire options
    seleniumwire_options = {
        'proxy': {
            'https': proxy_url
        }
    }

    # Set chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Get driver
    driver = webdriver.Chrome(
        seleniumwire_options=seleniumwire_options,
        chrome_options=chrome_options
    )


    driver.get(url=url)

    page_source = driver.page_source
    
    pdf_params = {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "scale": 1,
        "paperWidth": 8.5,
        "paperHeight": 11,
        "marginTop": 0,
        "marginBotton": 0,
        "marginLeft": 0,
        "marginRight": 0
    }

    data = driver.execute_cdp_cmd('Page.printToPDF', pdf_params)["data"]

    driver.close()

    return {
        "data": data,
        "page_source": page_source
    }

