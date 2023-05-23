### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
- RESTful routing is a series of naming conventions for routes used with HTTP requsts. It is used to make sure routes accurately describe what they do through their name, and are effective and reusable.

- What is a resource?
- A resource is a piece of data shared by an API or through an HTTP request. In a database for music tickets, each table could be considered a resource. 

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
- The purpose of a JSON API is to process and return JSON data. The JSON API can acknowledge form data, but the creation of the user would be done elsewhere.

- What does idempotent mean? Which HTTP verbs are idempotent?
- Idempotent is used to desribe an operation which will yield the same result each time it is executed. GET, HEAD, OPTIONS, TRACE, PUT, and DELETE are all idempotent HTTP requests.

- What is the difference between PUT and PATCH?
- PUT is used to with the addition of persisted data. Patch is used to update data already saved.

- What is one way encryption?
- One way encryption is hashing, where there is no key and the hashed plaintext cannot be decrypted.

- What is the purpose of a `salt` when hashing a password?
- Salt is random data used in hashing to further encrypt the plaintext.

- What is the purpose of the Bcrypt module?
- Bcrypt is used to securely store passwords or sensitive data via hashing.

- What is the difference between authorization and authentication?
- Authentication pertains to identity and authorization determines level of clearance or rights.
