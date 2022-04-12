# backend_challenge (Unfinished)

For this product, a valid quote will contain the following required fields:<br><br>
● Quote number<br>
○ A 10 digit mix of random letters and numbers used to uniquely identify
the quote. This is generated on the API side, not through API request
data.<br><br>
● Effective date<br>
○ The date coverage will begin if a policy is purchased.<br><br>
● Previous policy canceled<br>
○ Indicates if the customer has ever had a volcano insurance policy that
has been canceled.<br><br>
● Owns property to be insured<br>
○ Indicates if the customer owns the property to be insured.<br><br>
● Property address<br>
○ zipcode of the property to be insured.<br>
○ A valid US state<br><br>
Rating Algorithm<br>
● Base pricing for a Volcano Insurance policy is $59.94 for the entire 6 month
policy term.Additional Fees<br>
● If the policy holder has ever had a previous Volcano Insurance policy
canceled, an additional fee is applied in the amount of 15% of the base price.<br>
● If the policy holder!s property is in a state with a volcano, an additional fee is
applied in the amount of 25% of the base price, regardless of the distance the
property is from an active volcano.<br>
○ This fee is in addition to the fees mentioned above.<br>
○ US States with active volcanoes are:<br>
■ Alaska<br>
■ Arizona<br>
■ California<br>
■ Colorado<br>
■ Hawaii<br>
■ Idaho<br>
■ Nevada<br>
■ New Mexico<br>
■ Oregon<br>
■ Utah<br>
■ Washington<br>
■ Wyoming<br><br>
Additional Discounts<br>
● If the policy holder has never had a previous Volcano Insurance policy canceled,
a discount is applied in the amount of 10% of the base price.<br>
● If the policy holder owns the property to be insured, a discount is applied in the
amount of 20% of the base price.<br>

The Assignment<br>
Create a Django application that exposes a RESTful API with 2 endpoints:<br>
● one that allows a user to create a quote request for ACME!s new Volcano
Insurance product<br>
● one to "checkout” their quote request, and receive a detailed policy premium
rating for this quote.<br>
Follow the architectural guidelines below for all data model / API response
requirements.<br><br>
Endpoint 1 Architectural Guidelines: Request Quote EndpointDesign and implement an API endpoint that allows a user to create and persist a
quote request for the ACME Volcano Insurance product. For this challenge there is
no quote request update endpoint, so it can be safely assumed that a successful
create request results in creating and persisting a quote request on your API!s
backend with all required fields. Follow all principles of RESTful architecture when
designing this endpoint. Envision this endpoint being used in a production
environment from the standpoint of data validation, and error handling.<br><br>
Endpoint 2 Architectural Guidelines: Checkout Quote Endpoint
Design and implement an API endpoint that allows a user to fetch itemized policy
costs for a specific quote request. Follow all principles of RESTful architecture when
designing this endpoint. Envision this endpoint being used in a production
environment from the standpoint of data validation, and error handling. The expected
fields in the response body include:<br><br>
● Base premium<br>
○Base Premium for the entire policy term of 6 months.<br><br>
● Total term premium<br>
○ Total Premium for the entire policy term of 6 months including all Fees
and Discounts.<br><br>
● Monthly total premium<br>
○ Premium per month of a 6 month policy including all Fees and Discounts.<br><br>
● Total additional fees<br>
○ Sum total of any additional fees for the entire policy term of 6 months,
based on the policy rating requirements listed above.<br><br>
● Total monthly fees<br>
○ Total of any additional fees per month of a 6 month policy, based on the
policy rating requirements listed above.<br><br>
● Total discounts<br>
○ Sum total of any discounts based on the policy rating requirements
listed above.<br><br>
● Total monthly discounts<br>
○ Total of any discounts per month of a 6 month policy, based on the
policy rating requirements listed above.<br><br>
Other Guidelines<br>
● Your API should be written using Python 3 and Django 3 (preferably the latest
version of each).<br>
● Your API should be built following the principles of RESTful design.<br>
● Quotes created through your API should be persisted in a database (SQLite is
a good option, but you can use whatever you prefer).<br>
● Your API should have complete test coverage.<br>
● You do not need to do any frontend work for this assignment.<br>
● You are welcome to use any Python package (standard library and others) to help build
your API.<br>
● You should include a README outlining how to use your API and how to run
your test suite.<br>
