import requests
from bs4 import BeautifulSoup

# URL сайта с рецептами
url = "https://www.gastronom.ru/recipe" 


response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, "html.parser")

recipes = soup.find_all("div", class_="recipe-card")  

for recipe in recipes:
    title = recipe.find("h2", class_="recipe-title").text.strip()
    
    ingredients = recipe.find("ul", class_="ingredients").text.strip()
    
    print(f"Рецепт: {title}")
    print(f"Ингредиенты: {ingredients}")
    print("-" * 40)
