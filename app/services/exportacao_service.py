from .scraping_service import ScrapingService

# Instanciando a classe Scraping
exportacao_service_vinhos_mesa = ScrapingService(url_param='subopcao=subopt_01&opcao=opt_06')
exportacao_service_espumantes = ScrapingService(url_param='subopcao=subopt_02&opcao=opt_06')
exportacao_service_uvas_frescas = ScrapingService(url_param='subopcao=subopt_03&opcao=opt_06')
exportacao_service_suco_uva = ScrapingService(url_param='subopcao=subopt_04&opcao=opt_06')