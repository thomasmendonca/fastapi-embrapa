from .scraping_service import ScrapingService

# Instanciando a classe Scraping
processamento_service_viniferas = ScrapingService(url_param='subopcao=subopt_01&opcao=opt_03')
processamento_service_americanas = ScrapingService(url_param='subopcao=subopt_02&opcao=opt_03')
processamento_service_uvas = ScrapingService(url_param='subopcao=subopt_03&opcao=opt_03')
processamento_service_sem_classificacao = ScrapingService(url_param='subopcao=subopt_04&opcao=opt_03')