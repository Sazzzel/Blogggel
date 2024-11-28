
# Blogggel Portfolio and Developer Blog Website 

## Table of Contents

- [Introduction](#introduction)
- [Overview of the Project Purpose and Functionality](#overview-of-the-project-purpose-and-functionality)
- [User Experience (UX) Design](#user-experience-ux-design)
  - [Design Goals and Approaches](#design-goals-and-approaches)
  - [Typography and Fonts Used](#typography-and-fonts-used)
  - [Colour Palette](#colour-palette)
- [Wireframes](#wireframes)
  - [Mobile Wireframes](#mobile-wireframes)
  - [Tablet Wireframes](#tablet-wireframes)
  - [Desktop Wireframes](#desktop-wireframes)
- [User Stories](#user-stories)
  - [Visitor/User User Stories](#visitoruser-user-stories)
    - [User Story 1: User Registration](#user-story-1-user-registration)
    - [User Story 2: User Login](#user-story-2-user-login)
    - [User Story 3: Search Blogs by Programming Language](#user-story-3-search-blogs-by-programming-language)
    - [User Story 4: View Blog Posts](#user-story-4-view-blog-posts)
    - [User Story 5: Comment on Blog Posts](#user-story-5-comment-on-blog-posts)
    - [User Story 6: Edit Personal Profile](#user-story-6-edit-personal-profile)
    - [User Story 7: Like Blog Posts](#user-story-7-like-blog-posts)
    - [User Story 8: Bookmark Blog Posts](#user-story-8-bookmark-blog-posts)
    - [User Story 9: Receive Notifications](#user-story-9-receive-notifications)
    - [User Story 10: Responsive Design](#user-story-10-responsive-design)
  - [Admin User Stories](#admin-user-stories)
    - [Admin User Story 1: Create Blog Posts](#admin-user-story-1-create-blog-posts)
    - [Admin User Story 2: Read Blog Posts](#admin-user-story-2-read-blog-posts)
    - [Admin User Story 3: Update Blog Posts](#admin-user-story-3-update-blog-posts)
    - [Admin User Story 4: Delete Blog Posts](#admin-user-story-4-delete-blog-posts)
    - [Admin User Story 5: Moderate Comments](#admin-user-story-5-moderate-comments)
    - [Admin User Story 6: Manage Users](#admin-user-story-6-manage-users)
    - [Admin User Story 7: Review Reported Content](#admin-user-story-7-review-reported-content)
    - [Admin User Story 8: Manage Tags and Categories](#admin-user-story-8-manage-tags-and-categories)
    - [Admin User Story 9: View Site Analytics](#admin-user-story-9-view-site-analytics)
    - [Admin User Story 10: Configure Site Settings](#admin-user-story-10-configure-site-settings)
    - [Admin User Story 11: Add Article via API Endpoint](#admin-user-story-11-add-article-via-api-endpoint)
    - [Admin User Story 12: Update GitHub Repositories and Certificates](#admin-user-story-12-update-github-repositories-and-certificates)
    - [Admin User Story 13: Discord Bot Integration for Blog Posts](#admin-user-story-13-discord-bot-integration-for-blog-posts)
- [Features](#features)
  - [Home Page](#home-page)
  - [About Page](#about-page)
  - [Blog Page](#blog-page)
  - [Navigation Bar](#navigation-bar)
  - [Footer](#footer)
  - [Sign-Up Feature](#sign-up-feature)
  - [Sign-In Feature](#sign-in-feature)
  - [Sign-Out Feature](#sign-out-feature)
  - [Admin Features](#admin-features)
- [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Data Structure and Relationships](#data-structure-and-relationships)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Responsive Testing](#responsive-testing)
  - [Validator Testing](#validator-testing)
  - [Lighthouse Testing](#lighthouse-testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
    - [Install Django](#install-django)
    - [Creating An App](#creating-an-app)
    - [Prerequisites Before Deploying to Heroku](#prerequisites-before-deploying-to-heroku)
  - [Database Setup (PostgreSQL)](#database-setup-postgresql)
  - [Cloudinary](#cloudinary)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Clone the Project](#clone-the-project)
  - [Fork the Project](#fork-the-project)
- [Technologies & Languages Used](#Technologies-&-Languages-Used)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Features](#features-1)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)
- [Credits](#credits)
  - [Project Inspiration and Sources](#project-inspiration-and-sources)
  - [Content Creation Credits](#content-creation-credits)
  - [Media Credits](#media-credits)
- [No Contribution](#no-contribution)

![Description Header](docs/images/DescriptionHeader.png)

# Introduction
After spending a long time as a homemaker raising my children, I’ve decided to turn my long-time passion for programming into a career. This project represents a significant step in that journey—a way to combine the skills I’ve honed as a self-taught programmer with my dedication to lifelong learning.

Creating a full-stack development blog that integrates my GitHub repositories and a collection of certifications is more than just a technical challenge; it’s a personal statement. It’s a way to showcase my growth as a developer while reflecting my unique perspective and experiences. This project allows me to bring together modern backend development with Django, API integrations, and a dynamic, user-friendly frontend to build something practical and meaningful.

Choosing this as my capstone project felt natural because it’s not just a portfolio—it’s a bridge between the years I’ve spent nlearning from others and the career I’m building for myself. It demonstrates my ability to manage complex tasks, learn new technologies, and create something that celebrates both where I’ve been and where I’m headed.

- [Visit Site]()
- [Find me on LinkedIN](https://www.linkedin.com/feed/)

## User Experience (UX) Design


### Design Goals and Approaches

- Provide an intuitive and easy-to-navigate user interface.
- Maintain a professional, developer-focused aesthetic to appeal to potential employers and collaborators.

### Typography and Fonts Used



### Colour Palette

- The colour palette consists of:


[Back to Table of Contents](#table-of-contents)

## Wireframes


Wireframes were created to guide the layout of each key page of the website:


### Mobile Wireframes
- These are my mobile wireframes showing the individual website pages. (The Colours indicate different sections, not the final colours.)


### Tablet Wireframes
- These are my tablet wireframes showing the individual website pages. (The Colours indicate different sections, not the final colours.)



### Desktop Wireframes
- These are my Desktop wireframes showing the individual website pages. (The Colours indicate different sections, not the final colours.)


# User Stories


## User Stories - Table of Contents


---

## Visitor/User User Stories





---

## Admin User Stories





# Summary



---

**Next Steps:**



[User Story - Table of Contents](#User-Stories---Table-of-Contents)

[Back to Table of Contents](#table-of-contents)

## Features

### Home Page
- Displays a list of recent blog posts and highlights of portfolio projects.

### GitHub Page
- Provides insight into my background, interests, and motivations.

### Certifications Page
- Provides insight into my background, interests, and motivations.

### Blog Page
- Users can view all blog posts, search by programming languages, and see featured articles.

### Navigation Bar
- Available throughout the site with links to Home, Blog, About, and Contact pages.

### Footer
- Contains links to social media, quick navigation, and contact information.

### Sign-Up Feature
- Visitors can create an account to engage with content and personalize their experience.

### Sign-In Feature
- Registered users can log in to access member-only content and features.

### Sign-Out Feature
- Users can sign out, with their session safely terminated.

### Admin Features
- Admins can create, edit, delete posts, manage users, and moderate content.

[Back to Table of Contents](#table-of-contents)

## Entity Relationship Diagram

### Data Structure and Relationships
- The database is designed using PostgreSQL, with tables for Users, Blog Posts, Comments, Likes, Bookmarks, and Notifications. The Entity Relationship Diagram (ERD) shows the connections between these tables to ensure data integrity and support the features of the site.

[Back to Table of Contents](#table-of-contents)

## Testing

### Manual Testing
- Tested across various browsers, including **Chrome**, **Firefox**, **Edge**, and **Safari**.

### Responsive Testing
- Ensured the website is functional and visually appealing across devices such as desktops, tablets, and mobile phones.

### Validator Testing
- HTML, CSS, JavaScript, and Python code were validated using tools such as **W3C Validator**, **JSHint**, and **PEP8**.

### Lighthouse Testing
- **Google Lighthouse** was used to audit performance, accessibility, and SEO.

[Back to Table of Contents](#table-of-contents)

# Deployment

## Connecting to GitHub

To start this project from scratch, follow these steps to create a new GitHub repository using the Code Institute's Template. This template provides the necessary tools to set up your project:



## Django Project Setup

### Install Django


---

### Creating an app


---

###  Create Necessary Folders



### Prerequisites Before Deploying to Heroku




---

### Database Setup (PostgreSQL)


---

### Connecting to your database.



---

### Cloudinary




### Deploying to Heroku



[Back to Table of Contents](#table-of-contents)

---

## Clone the Project

To create a local clone of this repository from GitHub, follow these steps:


[Back to Table of Contents](#table-of-contents)

## Fork the Project
To create a copy of the original repository on your GitHub account, follow these steps:


[Back to Table of Contents](#table-of-contents)

# Technologies & Languages Used



[Back to Table of Contents](#table-of-contents)

# Features



---
[Back to Table of Contents](#table-of-contents)

# License

This project is licensed under the [MIT License](LICENSE).

---
[Back to Table of Contents](#table-of-contents)


# Contact

- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/sarah-darlington-dev/)
- **Email:** [your.email@example.com](mailto\:your.email@example.com)

---
[Back to Table of Contents](#table-of-contents)


# Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [GitHub Guides](https://guides.github.com/)

---
[Back to Table of Contents](#table-of-contents)

**Next Steps:**

1. **Add User Stories to Project Board:**

   - Create issues for each user story.
   - Include acceptance criteria and tasks in the issue description.

2. **Assign Tasks to Team Members:**

   - Distribute tasks based on expertise and workload.

3. **Set Milestones and Sprints:**

   - Organize user stories into sprints for iterative development.

4. **Implement Testing Strategies:**

   - Develop test cases based on acceptance criteria.
   - Use automated testing where possible.

5. **Monitor Progress and Metrics:**

   - Track completion of tasks.
   - Review test results to ensure quality.

By following this structured approach, you'll be able to efficiently develop your website with clear objectives and measurable outcomes. If you need assistance with any specific tasks or have further questions, feel free to ask!

[User Story - Table of Contents](#user-stories---table-of-contents)

[Back to Table of Contents](#table-of-contents)

## Credits

### Project Inspiration and Sources
- This project was inspired by my journey as a developer and my desire to create a comprehensive platform to showcase my work and certifications.

### Content Creation Credits
- Blog posts and portfolio descriptions are original content written by myself, augmented with AI tools where needed.

### Media Credits
- Icons are sourced from **Font Awesome**, 
- Images are either created by myself or sourced from royalty-free platforms like **Unsplash** and **Pexels**.

[Back to Table of Contents](#table-of-contents)



# No Contribution

## This is a Capstone Project for the Code Institute.

Therefore, no contribution is required. Thank you anyway!

[Back to Table of Contents](#table-of-contents)