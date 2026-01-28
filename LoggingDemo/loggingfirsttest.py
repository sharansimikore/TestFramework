import logging
# logging.basicConfig(level=logging.DEBUG, filename='denologs.log', filemode='a')
logging.basicConfig(level=logging.DEBUG, filename='..\\demologs.log', filemode='w', format='%(asctime)s - %(levelname)s : %(message)s)')

class Demologging:
    def add_numbers(self, a, b):
        return a + b

    def multiply_numbers(self, a, b):
        return a * b

total_numbers = Demologging()
result=total_numbers.add_numbers(1, 2)
logging.warning("Addition of two numbers: {}" .format(result))
logging.debug("Addition of two numbers: {}" .format(result))
logging.error("Addition of two numbers: {}" .format(result))
logging.critical("Addition of two numbers: {}" .format(result))
logging.info("Addition of two numbers: {}" .format(result))


result=total_numbers.multiply_numbers(3, 4)
logging.warning("Multiplication of three numbers: {}" .format(result))