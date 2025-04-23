from .scraping_service import ScrapingService

# Instanciando a classe Scraping
importacao_service_vinhos_mesa = ScrapingService(url_param='opcao=opt_05')
importacao_service_espumantes = ScrapingService(url_param='subopcao=subopt_02&opcao=opt_05')
importacao_service_uvas_frescas = ScrapingService(url_param='subopcao=subopt_03&opcao=opt_05')
importacao_service_uvas_passas = ScrapingService(url_param='subopcao=subopt_04&opcao=opt_05')
importacao_service_suco_uva = ScrapingService(url_param='subopcao=subopt_05&opcao=opt_05')
