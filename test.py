import logging

# Show all logging levels, including DEBUG and INFO
logging.basicConfig(level=logging.DEBUG)

logging.debug("Checking product price")
logging.info("Product page opened")
logging.warning("Product price is missing")
logging.error("Product update failed")
logging.critical("Automation cannot continue")
print("=" * 70)
# using print
print("DEBUG:root:Checking product price")
print("INFO:root:Product page opened")
print("WARNING:root:Product price is missing")
print("ERROR:root:Product update failed")
print("CRITICAL:root:Automation cannot continue")