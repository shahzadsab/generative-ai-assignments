import logging

extData = {'user': 'sbhatti@example.com'}

def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


def main():
    # Use basicConfig to configure logging
    # this is only executed once, subsequent calls to
    # basicConfig will have no effect
    # print(logging.__file__)    
    # logging.basicConfig(level=logging.DEBUG,
    #                     filemode="w",
    #                     filename="output.log")
    
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="samples/output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    
    # Try out each of the log levels
    # logging.debug("This is a debug-level log message")
    # logging.info("This is an info-level log message")
    # logging.warning("This is a warning-level message")
    # logging.error("This is an error-level message")
    # logging.critical("This is a critical-level message")

    # Output formatted string to the log
    # logging.info("Here's a {} variable and an int: {}".format("string", 10))
    
    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()



if __name__ == "__main__":
    main()
