from models.company import Company
import logging

class CompanyController:
    @staticmethod
    def add_company(name, description, factory_code):
        """
        Add a new company to the database

        :param name: str
        :param description: str
        :param factory_code: int
        
        :returns: Company
        """
        if Company.select_by_name(name):
            raise ValueError("Company already exists")
        if Company.select_by_factory_code(factory_code):
            raise ValueError("Company with this factory code already exists")
        
        try:
            company = Company(name, description, factory_code)
            company.save()
            logging.info(f"Company {name} added successfully")
            return company
        except Exception as e:
            logging.error(f"Error adding company: {e}")
            raise e
    
    @staticmethod
    def get_companies():
        """
        Get all company from the database

        :returns: list
        """
        return Company.select_all()