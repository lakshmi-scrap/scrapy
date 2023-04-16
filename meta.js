const puppeteer = require('puppeteer');
const fs = require('fs');

async function scrapeJobs() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://www.metacareers.com/jobs');

  const jobTitles = await page.$$eval('._8sef', titles => titles.map(title => title.innerText.trim()));
  const jobLocations = await page.$$eval('._8see _97fe', locations => locations.map(location => location.innerText.trim()));
  const jobDescription = await page.$$eval('._9ata _8ww0', description => description.map(description => description.innerText.trim()));

  const jobs = [];

  for (let i = 0; i < jobTitles.length; i++) {
    jobs.push({
      title: jobTitles[i],
      location: jobLocations[i],
      description: jobDescription[i]
    });
  }

  const json = JSON.stringify(jobs);

  fs.writeFile('jobs.json', json, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Data written to file');
  });

  await browser.close();
}

scrapeJobs();
