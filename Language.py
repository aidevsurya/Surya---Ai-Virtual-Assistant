import argostranslate.package as argo_package
import argostranslate.translate as argo_translate

from_lang = "en"
to_lang = "hi"

# argo_translate.package.update_package_index()
# available_packages = argo_translate.package.get_available_packages()
# package_to_install = next(
#     filter(
#         lambda x: x.from_code == from_lang and x.to_code == to_lang, available_packages
#     )
# )

# argo_translate.package.update_package_index()
# available_packages = argo_translate.package.get_available_packages()
# package_to_install = next(
#     filter(
#         lambda x: x.from_code == to_lang and x.to_code == from_lang, available_packages
#     )
# )

# argo_translate.package.install_from_path(package_to_install.download())

def translate(text,from_lang="en",to_lang="hi"):
    text = argo_translate.translate(text,from_code=from_lang,to_code=to_lang)
    return text