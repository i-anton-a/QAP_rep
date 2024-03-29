import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(autouse=True, scope="session")
def testing():
   # вместо 'C:/Skillfactory/chromedriver.exe' укажите путь к веб-драйверу
   # В случаи Linux путь будет приблезительно таким /home/<username>/selenium/chromedriver
   # В примере оставил для ОС windows
   pytest.driver = webdriver.Chrome('C:/Skillfactory/chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

      # почта и пароль для пользователя под которым проивходиться вход
   pytest.driver.find_element(By.ID, 'email').send_keys('user98@user.com')
   pytest.driver.find_element(By.ID, 'pass').send_keys('user98')
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
   yield

   pytest.driver.quit()

def test_check_my_pets():
   #Проверяем, что открыта страница "Мои питомцы" по имени пользователя
   assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text != ""

def test_check_my_pets_amount(driver):
   #Проверяем, что количество питомцев одинаково что в таблице что в статистике пользователя
   #количество питомцев в таблице по количеству строк
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']")))
   my_pets = pytest.driver.find_elements(By.XPATH, "//th[@scope='row']")

   #количество питомцев из статистики пользователя
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='.col-sm-4 left']")))
   user_info = pytest.driver.find_element(By.XPATH, "//div[@class='.col-sm-4 left']").text
   user_info = user_info.split('\n')
   pet_number = int(user_info[1].split(': ')[1])

   try:
      assert len(my_pets) == pet_number
   except:
      raise Exception("Количество питомцев не совпадает с данными в статистике пользователя.")

def test_at_least_half_my_pets_has_photo(driver):
   #Провекра, что как минимум у половины питомчев есть фото
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@scope='row']/img")))
   images = pytest.driver.find_elements(By.XPATH, "//th[@scope='row']/img")

   #не пустые картинки
   images_counter = 0

   # половина от количества питомцев пользователя с функцией из библиотеки math для арифметического округления
   my_pets_half = math.ceil(len(images) / 2)

   # подсчет питомцев пользователя у которых есть фото
   for image in range(len(images)):
      if images[image].get_attribute('src') != '':
         images_counter += 1

   try:
      assert images_counter >= my_pets_half
   except:
      raise Exception("Меньше половины питомцев пользователя имеют фото.")

def test_my_pets_all_info():
   # Проверка на наличие имя, парода, и позраст питомца
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr/td[1]')))
   names = pytest.driver.find_elements(By.XPATH, '//tr/td[1]')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr/td[2]')))
   breeds = pytest.driver.find_elements(By.XPATH, '//tr/td[2]')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr/td[3]')))
   ages = pytest.driver.find_elements(By.XPATH, '//tr/td[3]')

   for i in range(len(names)):
      try:
         assert names[i].text != ''
         assert breeds[i].text != ''
         assert ages[i].text != ''
      except:
         raise Exception("У пользователя есть питомец с пустыми данными.")

def test_unique_pet_names(driver):
   #Проверка что у питомцев разные имена
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr/td[1]')))
   names = pytest.driver.find_elements(By.XPATH, '//tr/td[1]')

   #уникальные имена
   unique_pet_names = []

   #поиск уникальных имен и добавление их в отдельный список
   for e in range(len(names)):
      if names[e].text not in unique_pet_names:
         unique_pet_names.append(names[e].text)

   try:
      assert len(names) == len(unique_pet_names)
   except:
      raise Exception("В списке питомцев пользователя есть повторябщие имена")

def test_unique_pets(driver):
   # Проверка питомцев на уникальных питомцев
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr/td[1]')))
   names = pytest.driver.find_elements(By.XPATH, '//tr/td[1]')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr/td[2]')))
   breeds = pytest.driver.find_elements(By.XPATH, '//tr/td[2]')
   WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr/td[3]')))
   ages = pytest.driver.find_elements(By.XPATH, '//tr/td[3]')

   #неуникальные питомцы
   non_unique_pets_counter = 0

   #подсчет питомцев с одинаковым именем, породой, возрастом
   for x in range(len(names) - 1):
      for y in range(x + 1, len(names)):
         if names[x].text == names[y].text:
            if breeds[x].text == breeds[y].text:
               if ages[x].text == ages[y].text:
                  non_unique_pets_counter += 1
   try:
      assert non_unique_pets_counter == 0
   except:
      raise Exception("В списке есть повторяющиеся питомцы (с одинаковым именем, породой и возрастом)")
