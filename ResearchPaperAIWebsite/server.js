const DEFAULT_VALUE = 'n/a'

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const rateLimit = require('express-rate-limit');
const { body, validationResult } = require('express-validator');
const cors = require('cors');
const {ChartJSNodeCanvas} = require('chartjs-node-canvas');


require('dotenv').config();

const PORT = 8000;

app.set('view engine', 'ejs');

app.use(express.static('public'));
app.use('/css', express.static(__dirname + 'public/css'));
app.use('/assets', express.static(__dirname + 'public/assets'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());
app.use(express.json());

// const limiter = rateLimit({
// 	windowMs: 1000,
// 	max: 1
// });

// app.use(limiter);

app.locals.getID = function(val) {
	return val.split('/').pop();
};

function swapJsonKeyValues(json){
	let ret = {};
	let abstractResult = "";

	for(var key in json){
		for(let i = 0; i < json[key].length; i++) {
			ret[json[key][i]] = key;
		}
	}

	for(var nam in ret) {
		abstractResult += `${ret[nam]} `
	}
	
	return abstractResult;
}

async function createGraph(arrObjInput) {
	const width = 600;   // define width and height of canvas 
	const height = 600;   
	const backgroundColor = 'white'; 
	const chartJSNodeCanvas = new ChartJSNodeCanvas({width, height, backgroundColor});

	let xAxisArr = [];
	let yAxisArr = [];

	arrObjInput.forEach(element=> {
		xAxisArr.push(element.year);
		yAxisArr.push(element.cited_by_count);
	})

	const configuration = {
		type: 'bar',
		data: {
			labels: xAxisArr,
			datasets: [{
				label: '# of papers cited by this work',
				data: yAxisArr,
				backgroundColor: [
					'rgba(255, 90, 0, 0.4)'
				],
				borderColor: [
					'rgba(255, 90, 0, 1)'
				],
				borderWidth: 1
			}]
		},
		options: {
			scales: {
				x: {
					title: {
						display: true,
						align: 'center',
						text: 'Years'
					  }
				},
				y: {
					title: {
						display: true,
						align: 'center',
						text: '# of papers cited by this work'
					  }
				}
			}
		},
		plugins: [{
			id: 'background-color',
			beforeDraw: (chart) => {
				const ctx = chart.ctx;
				ctx.save();
				ctx.fillStyle = 'white';
				ctx.fillRect(0, 0, width, height);
				ctx.restore();
			}
		}]
	};

	const dataUrl = await chartJSNodeCanvas.renderToDataURL(configuration); // converts chart to image
	return dataUrl;
}

app.get("/", (req, res) => {
	try {
		res.sendFile(__dirname + '/index.html');

	} catch (err) {
		console.log( err.message);
		res.sendFile(__dirname + '/index.html');
	}
})

app.post('/search/', (req, res) => {
    res.redirect('search/' + req.body.search);
})

//for querying on keywords
app.get("/search/:query", async (req, res) => {
	try {
		const apiURL = `https://api.openalex.org/works?search=${req.params.query}?page=1`;
		const fetchResponse = await fetch(apiURL);
		const jsonResults = await fetchResponse.json();

		//check for possible value that does not exist, returns http 404

		const results = jsonResults['results']
		.map(a => ({ 
			id: a.id ? a.id : '[Missing ID]', 
			title: a.title ? a.title : '[Missing Title]', 
			publication_year: a.publication_year ? a.publication_year : '[Missing publisher year]',
			type: a.type ? a.type : '[Missing Type]',
			is_retracted: a.is_retracted ? a.is_retracted : DEFAULT_VALUE,
			is_paratext: a.is_paratext ? a.is_paratext : DEFAULT_VALUE,
			authorships: a.authorships ? a.authorships : DEFAULT_VALUE 
		}));	
		
		res.render('search.ejs', { paper: results });

	} catch (err) {
		console.log( err.message);
		res.render('search.ejs', { paper: null});
	}
})

app.get("/paper/:paperID", async (req, res) => {
	try {
		const apiURL = `https://api.openalex.org/works/${req.params.paperID}`;
		const fetchResponse = await fetch(apiURL);
		let jsonResults = await fetchResponse.json();

		//check for possible value that does not exist, returns http 404

		//cited works only gets up to 25 works
		// const citedWorksURL = `https://api.openalex.org/works?filter=cited_by:${req.params.paperID}`
		// const fetchCitedWorks = await fetch(citedWorksURL);
		// const citedWorksResults = await fetchCitedWorks.json();

		// const citedWorks = citedWorksResults['results']
		// .map(a => ({ 
		// 	title: a.title ? a.title : '[Missing Title]', 
		// 	publication_year: a.publication_year ? a.publication_year : '[Missing publisher year]',
		// 	type: a.type ? a.type : '[Missing Type]'
		// }));

		//get the IDs from each url
		jsonResults.referenced_works.forEach(function(workUrl, index) {
			this[index] = app.locals.getID(workUrl);
		}, jsonResults.referenced_works);

		//ensures data is in ascending order by 'year'
		jsonResults.counts_by_year.sort(function(a, b){
			return a.year - b.year;
		});

		const results = {
			id: req.params.paperID, 
			doi: jsonResults.doi ? jsonResults.doi : DEFAULT_VALUE, 
			title: jsonResults.title ? jsonResults.title : '[No Title]', 
			relevance_score: jsonResults.relevance_score ? jsonResults.relevance_score : DEFAULT_VALUE,
			publication_year: jsonResults.publication_year ? jsonResults.publication_year : DEFAULT_VALUE,
			host_venue_pub: jsonResults.host_venue.publisher ? jsonResults.host_venue.publisher : DEFAULT_VALUE,
			type: jsonResults.type ? jsonResults.type : DEFAULT_VALUE,
			open_access: jsonResults.open_access.is_oa ? jsonResults.open_access.is_oa : DEFAULT_VALUE,
			biblio_first: jsonResults.biblio.first_page ? jsonResults.biblio.first_page : DEFAULT_VALUE,
			biblio_last: jsonResults.biblio.last_page ? jsonResults.biblio.last_page : DEFAULT_VALUE,
			is_retracted: jsonResults.is_retracted ? jsonResults.is_retracted : DEFAULT_VALUE,
			is_paratext: jsonResults.is_paratext ? jsonResults.is_paratext : DEFAULT_VALUE,
			authorships: jsonResults.authorships ? jsonResults.authorships : DEFAULT_VALUE,
			concepts: jsonResults.concepts ? jsonResults.concepts : DEFAULT_VALUE,
			referenced_works: jsonResults.referenced_works,
			counts_by_year: jsonResults.counts_by_year ? jsonResults.counts_by_year : DEFAULT_VALUE,
			abstract: swapJsonKeyValues(jsonResults.abstract_inverted_index),
			graphy: await createGraph(jsonResults.counts_by_year)
		};

		res.render('paper.ejs', { paper: results });

	} catch (err) {
		console.log( err.message);
		res.render('paper.ejs', { paper: null});
	}
})

app.listen(process.env.PORT || PORT, () => {
    console.log(`The server is running on ${PORT}!`);
})