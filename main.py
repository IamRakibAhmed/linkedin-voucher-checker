from utils.logger import setup_logger
from utils.file_handler import load_urls, update_urls_file
from services.linkedin_service import LinkedInService

def main():
    # Initialize logger
    logger = setup_logger()

    # Load URLs
    urls = load_urls()
    logger.info(f"Loaded {len(urls)} URLs.")

    # Initialize LinkedIn service
    linkedin_service = LinkedInService(logger)
    linkedin_service.login()

    valid_urls = []

    # Process each URL
    for i, url in enumerate(urls):
        status = linkedin_service.check_url(url)
        logger.info(f"URL: {url} - Status: {status}")

        if status == "Unchecked":
            logger.warning(f"Encountered 'Something went wrong' at URL: {url}")
            update_urls_file(urls[i:])
            linkedin_service.close()
            exit()

        if status == "Valid":
            valid_urls.append(url)

    # Save valid URLs to a new file
    if valid_urls:
        from pandas import DataFrame
        DataFrame(valid_urls, columns=["Valid URLs"]).to_excel("valid_urls.xlsx", index=False)
        logger.info("Valid URLs saved to valid_urls.xlsx.")

    linkedin_service.close()
    logger.info("Script finished successfully.")

if __name__ == "__main__":
    main()
