# Somi - Online School For The Next Generation Student

Somi is a web application designed and built as an e-learning platform with a content management system (CMS) that provides tools to for Instructors to generate content with flexibility in mind, where students can register and enroll to courses with dynamic and interactive content, discuss with other students and the course instructor in a chatroom all while efficiently taking notes, access them, and compartmentalize them into appropriate courses, academic terms, and their specific schools

## Features

    1. A flexible online CMS that allows instructors to create courses and manage their contents
    2. A Student centered platform for offering dynamic content from Videos, Text, PDF files, and Images.
    3. Our e-learning platform will offer courses and modules on various subjects. 
    4. Chat functionality for each course chatroom
    5. A great note keeping dashboard for students with a wide array of input fields
    6. A fully featured API for Client side Applications (Mobile, Maybe JS Framework Frontend)
    7. Additional Mobile app (Android) for course views

### Packages

All packages for the development of this project are contained in the *requirements.txt* file above.

#### Milestones and Code-Checklist

#### Core Functionalities

#### ✅ Functionality for instructors

* [x] 1. Setting up the e-learning project
* [x] 2. Building the course app models and Registering the models in the administration site
* [x] 3. Using fixtures to load Subjects data.
* [x] 4. Creating models for diverse content-types (Video, Files, Text, Images)
* [x] 5. Adding ordering to module and content objects
* [x] 6. Adding an authentication system (Only Login and Logout)
* [x] 7. Using custom mixins in views for Working with groups and permissions (Instructors, Students)
* [x] 8. Using formsets for course modules
* [x] 9. Adding content to course modules
* [x] 10. Managing and Reordering modules and their contents (AJAX-based drag-and-drop functionality to order course modules and their contents)

#### Rendering, Accessing and Caching Course Contents (Student View)

* [x] 1. Displaying courses (Filter by subject and displaying a single course overview)
* [x] 2. Adding student registration view
* [x] 3. Enrolling to courses and Accessing the course contents
* [x] 4. Rendering different content-types (Video, Files, Text, Images)
* [ ] Cache Backends Framework for Rendering and Caching Content - *Memcached*
* [ ] Cache settings - Adding Memcached
* [ ] Low-level cache API
* [ ] Caching based on dynamic data
* [ ] Caching template fragments
* [ ] Caching views
* [ ] Using the per-site cache

#### Payment app

* [x] 1.Payment app, and MPESA API boilerplate
* [x] 2.Payment Logic and monthly subscription
* [ ] 3.Free 7 day trial
* [ ] 4.Decorators
* [ ] 5.Model Mixins to restrict course views on an only Paid aceess or free trial

##### Secondary Features (Chat, Notes, API)

##### Building an API for Mobile and or other clients

* [ ] Setting up Django REST framework
* [ ] Defining serializers (parsers and renderers)
* [ ] Building list and detail views
* [ ] Creating nested serializers
* [ ] Building custom API views
* [ ] Handling authentication and Permissions
* [ ] Viewsets and routers
* [ ] Prep: Consuming the RESTful API

##### Intergrating Notes App

* [ ] Merging auth system
* [ ] Notes Models
* [ ] Notes url routes
* [ ] Note Views
* [ ] REST API for Notes

##### Building the Chat Server

* [ ] Creating a chat application
* [ ] Implementing the chat room view
* [ ] Deactivating the per-site cache
* [ ] Asynchronous applications using ASGI and Django with Channels
* [ ] Writing chat.consumer
* [ ] Routing
* [ ] Implementing the WebSocket client
* [ ] Enabling a channel layer with Redis
* [ ] Updating the consumer to broadcast messages
* [ ] Adding context to messages
* [ ] Modifying the consumer to be fully asynchronous
* [ ] Integrating the chat application with existing views

##### Building Better User Interfaces

* [ ] Structuring Interfaces for Core, Courses, Students, Notes, Chat apps
* [ ] Filling In the Gaps
* [ ] Redirecting and Auth Views
* [ ] Public Views -core
* [ ] Handling layout static components (Carousel, Testimonials, Partners, Contact us)
* [ ] Map
* [ ] Footer and Newsletter form
* [ ] Contact Us

#### Deployment

* [ ] Creating a production environment
* [ ] Using PostgreSQL
* [ ] Serving Django through WSGI
* [ ] Installing and Configuring NGINX to serve static files
* [ ] Serving static and media assets
* [ ] Securing connections with SSL/TLS
* [ ] Redirecting HTTP traffic over to HTTPS
* [ ] Using Daphne for Django Channels, Including Daphne in the NGINX configuration
* [ ] Using secure connections for WebSockets
* [ ] Creating a subdomain middleware
* [ ] Serving multiple subdomains with NGINX
* [ ] Implementing custom management commands
* [ ] 🚀 Going Live!

##### What's next?

* Optimizing the app
* Building an Android App to consume the API
* Adding Blog Functionality
* Maybe adding a specialized React Frontend
