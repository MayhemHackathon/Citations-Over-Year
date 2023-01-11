Open Alex Data Structure
 1. ID (label) 			<DONE>
 2. DOI (future ref)		<DONE>
 3. Title				<DONE>
 4. Publication Year		<DONE>
 5. Host Venue (Publisher)	<DONE>
 6. Type (Journal, Article)	<DONE>
 7. Open Access (isOA)		<DONE>
 8. Authorship (Author / institution)	<DONE>
 	a. Author Name		<DONE>
 9. Biblio \/ In journal, page count	<DONE>
	a. First Page		<DONE>
	b. Last Page 		<DONE>
 10. Concepts			<DONE>
	a. Display Name		<DONE>
	b. Level			<DONE>
	c. Score			<DONE>
 11. Referenced Works (count vs combined citation count) <DONE>
 12. Counts by Year (cumulative)
 13. Abstract

PREVIEW section
	Title
	Type
	Publisher Year
	Author(s)

Filters
isRetracted and isParatext

Pagination
<< 1 ... [n-2] [n-1] [n] [n+1] [n+2] ...  Max >>

To Dos
	> Sanitize user inputs and all possible roots
	> Test again for page responsiveness
	> Handle potential 404 errors
	> Refactor CSS rules
	> Add filter support
	> Add pagination support (fix spacing around it)
		> Ensure first page of results is truly 'page 1' in api call
	> On paper.ejs, add back button
	> Do test on all route paths indepedently
	> Generalize createGraph() in server.js

Installing packages nice-to-knows
	> Ensure you execute this in terminal: npm i chartjs-node-canvas chart.js. Do not import
	these 2 packages separately as the above command will import versions that will be compatible with each other.
	Simply uninstall the separate install and run with the above command