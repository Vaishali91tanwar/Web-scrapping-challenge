# Mission to Mars

<img src="Mars_image.jpg">
<h3>Objective:</h3>

To build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

<h3>Data Sources:</h3> 

1. <strong>NASA Mars News:</strong> https://mars.nasa.gov<br>
2. <strong>JPL Mars Space Images- Featured Images:</strong> https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
3. <strong>Mars Weather:</strong> https://twitter.com/marswxreport?lang=en
4. <strong>Mars Facts:</strong> https://space-facts.com/mars 
5. <strong>Mars Hemispheres:</strong> https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

<h3>Methodology:</h3>
<hr>
<ul>
  <li>Initial scraping of the above websites for latest news headline and snippet, featured image, latest weather tweet, fact table and hemisphere images is done using Jupyter notebook, BeautifulSoup, Pandas and Requests/Splinter.</li><br><br>
  
  <li>Converting Jupyter notebook into a Python script with a function called scrape that executes all the scraping code from above and returns one Python dictionary containing all of the scraped data.</li>
  
  <li>Flask App route "/scrape" calls the scrape function and stores the returned Python dictionary into the MongoDB</li>
  
  <li>Flask app route "/" then queries the Mongo database and pass the mars data into an HTML template to display the data.</li>






Beautiful soup was used to scrape the above websites for latest news headline and snippet, featured image, latest weather tweet, fact table and hemisphere images respectively.
The scrapped data was then stored in MongoDB and was rendered onto the HTML page using flask app. 
A user interactive button was provided on the page which on clicking would scrape the latest information and render it on the page.<br><br>
<img src="mars1.JPG"><br><br>
<img src="mars2.JPG">
