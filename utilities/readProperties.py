import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\ckart\PycharmProjects\pythonProject1\NewProjectFrameWork\Configurations\config.ini")

class ReadConfig:
    @staticmethod
    def Get_Application():
        url = config.get("common info","baseurl")
        return url
    @staticmethod
    def firstname():
        firstname = config.get("common info","firstname")
        return firstname
    @staticmethod
    def lastname():
        lastname = config.get("common info","lastname")
        return lastname
    @staticmethod
    def email_id():
        email = config.get("common info","email")
        return email
    @staticmethod
    def Password():
        password = config.get("common info","password")
        return password
    @staticmethod
    def confirm_pass():
        conf_pass = config.get("common info","conf_pas")
        return conf_pass



