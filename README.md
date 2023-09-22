# 📃 About
The Django-Learning-System is a Django / DRF based API that implements a platform for learning through video courses.

The project provides the following endpoints:
* Obtaining an authentication token:
  * /token/
* A list of all available user lessons:
  * /lessons/all/
* A list of all available user lessons for a specific product: 
  * /lessons/product/1/
* Statistics for each product:
  * /products/statistics/
 
Database diagram: https://dbdiagram.io/d/Django-Learning-System-650d5ac8ffbf5169f04c0438

> The project was created as a test task.

# 💽 Installation

1. #### Clone or download the repository.
2. #### Rename .env.dist to .env and populate it with all variables or just leave test ones.
3. #### Run docker services: `docker-compose up -d`

# 🌄 Demonstration

### A list of all available user lessons:
![Postman_NkLGiNrFgj](https://github.com/FCTL3314/Django-Learning-System/assets/97694131/3af78105-3a1f-4078-a67c-ed798003d57f)

### A list of all available user lessons for a specific product: 
![Postman_wpWEyzH9cJ](https://github.com/FCTL3314/Django-Learning-System/assets/97694131/7f59566b-1ecd-44c5-83b1-b6eaa5567702)

### Statistics for each product:
![Postman_9Z73OOpIZF](https://github.com/FCTL3314/Django-Learning-System/assets/97694131/87564b86-48fc-4b8b-a114-9f504f3e024e)

