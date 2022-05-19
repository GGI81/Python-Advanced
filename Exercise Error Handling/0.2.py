from ERRORS import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

valid_domains = {"com", "bg", "net", "org"}

while True:
    line = input()
    if line == "End":
        break

    # peter@gmail.com
    # petergmail.com
    # peter@gmail
    email_prats = line.split("@")
    if len(email_prats) == 1:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email_prats) != 2:
        raise MustContainAtSymbolError("Email must contain only one @ sign")

    name, domain_name = email_prats

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = domain_name.split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError(
            f"{domain} is not valid domain. Domain must be one of the following: .com, .bg, .org. .net")

    print("Email is valid")

