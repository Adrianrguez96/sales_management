# /controllers/company_controller.py

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
    
    @staticmethod
    def search_company(search_option, search_input):
        """
        Search for companies in the database

        :params
            search_options: list
            search_input: str

        :returns: list
        """

        if not search_input:
            raise ValueError("Search input cannot be empty")

        match search_option:
            case "Name":
                return Company.select_by_partial_name(search_input)
            case "Factory code":
                return Company.select_by_partial_factory_code(search_input)
            case "Creation Date":
                return Company.select_by_creation_date(search_input)
            case "Last Update":
                return Company.select_by_last_update(search_input)
            case _:
                raise ValueError("Search option not found")