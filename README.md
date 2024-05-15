# SeoAgency

![Main](media/readme/hero.jpg)
Visit the [live site](https://agency-8f506ba47bf6.herokuapp.com/)

SeoAgency is a prototype of a commercial website that was developed as part of the Full-Stack Software Development Course at the Code Institute. The primary objective of this project was to create a foundational website that, with specific enhancements, could be fully utilized in a professional setting.

The core purpose of the commercial website is to attract clients. It features key sections such as Services and a Price List. The Services page is designed to generate leads; clicking on any service directs users to a contact form. This form not only records inquiries in a database but also optionally interacts with a CRM system, facilitating seamless customer relationship management.

The Price List page focuses on a main offering: SEO support for online projects. It allows users to view different service packages, choose one, and subscribe via a sandboxed PayPal integration, demonstrating the site's e-commerce capability. Additionally, the site includes a subscription form powered by [Mailtrap](https://mailtrap.io)  in email testing mode, ensuring reliable email delivery testing during the development phase.

Future plans for the project include deploying it on a real domain, expanding the Services page to enhance client trust through a portfolio page, and integrating a chatbot for immediate communication with potential customers. This approach aims to solidify SeoAgency as a robust tool for businesses seeking effective online presence management.

## User Stories Documentation

### Introduction

This document outlines the user stories developed for the project, structured to guide the development process and feature prioritization. The user stories define the functionalities that will provide the most value to both the users and the business during the initial phases of the project.

### Prioritization Framework

I have employed the MoSCoW method for prioritizing the user stories to ensure that we focus on delivering the most critical features first. This method categorizes features into:

- **Must have**: Essential features that are required for launch.
- **Should have**: Important but not necessary for launch.
- **Could have**: Desirable but not necessary and could improve user experience or customer satisfaction.
- **Won't have this time**: Agreed upon not to be developed in this release cycle.

### MVP Scope

The following key functionalities are defined as part of the MVP to streamline the development process and ensure a timely launch:

- **Must have** tasks, including:
  - Setup and Deploy
  - Home Page Interaction
  - Subscription Management

- **Should have** tasks, including:
  - Contact Us Page Interaction
  - Services Interaction
  - Admin Update Service

- **Could have** tasks, not implemented in the MVP due to prioritization:
  - Change Password
  - Update Profile
  - Collect Feedback

These tasks have been deferred to post-launch phases or future updates based on their current priority status and resource allocation. They are recognized as valuable but not essential for the initial launch.

### Assignees

I am assigned to crucial tasks that align with the MVP's strategic goals, focusing on ensuring robust core functionalities are implemented and tested before the initial rollout.

### Conclusion

The use of the MoSCoW method has allowed us to clearly define and communicate the project's scope and necessary resources. By focusing on the 'Must have' and 'Should have' categories, we aim to launch with a solid foundation while leaving room for scalability and future enhancements.

## User Stories

### Epic 1: User Account Management

#### 1. Create an Account (MUST)

- **Name:** CreateAccount
- **Title:** Enable users to create a new account
- **Description:** "As a user, I want to be able to create an account so that I can have a personalized experience on the website."
- **Acceptance Criteria:**
  1. The user can access a registration form from the homepage.
  2. The registration form requires a username, email, and password.

#### 2. Log In (MUST)

- **Name:** LogIn
- **Title:** Enable user login for account access
- **Description:** "As a user, I want to be able to log in to my account so that I can access my personal settings."
- **Acceptance Criteria:**
  1. The user can access a login form from the header.
  2. The login form requires a name and password.
  3. The user is redirected to their home upon successful login.

#### 3. Log Out

- **Name:** LogOut
- **Title:** Allow users to securely log out
- **Description:** "As a user, I want to be able to log out of my account so that I can ensure my account is secure when not in use."
- **Acceptance Criteria:**
  1. The logout option is easily accessible from the user's menu page.
  2. The user is redirected to the homepage after logging out.

#### 4. Update Profile (COULD)

- **Name:** UpdateProfile
- **Title:** Allow users to update their profile information
- **Description:** "As a user, I can update my profile information so that I can keep my personal information up to date."
- **Acceptance Criteria:**
  1. The user can access their profile settings from their dashboard.
  2. The user can update information such as their name, email, and password.
  3. Changes are saved immediately after the user confirms the update.

#### 5. Change Password (COULD)

- **Name:** ChangePassword
- **Title:** Allow users to change their password
- **Description:** "As a user, I can change my password so that I can ensure my account's security is up to date."
- **Acceptance Criteria:**
  1. The user can access a change password option from their profile settings.
  2. The user must enter their current password and a new password twice for confirmation.

### Epic 2: Website Interaction

#### 1. Home Page Interaction (MUST)

- **Name:** HomePageInteraction
- **Title:** Enhance user interaction with an engaging and informative home page
- **Description:** "As a user, I want to easily find information about SeoAgency and enjoy interacting with a dynamic home page so that I can have a positive experience and be motivated to explore further."
- **Acceptance Criteria:**
  1. The home page prominently features information about SeoAgency, including services and achievements.
  2. Interactive elements such as sliders, hover effects, and dynamic content are implemented to engage users.
  3. Navigation is intuitive, allowing users to easily find additional content and resources.
  4. The design and layout of the home page are visually appealing and aligned with the brand's image.

#### 2. Contact Us Page Interaction (SHOULD)

- **Name:** ContactUsPageInteraction
- **Title:** Facilitate user interaction with a comprehensive Contact Us page
- **Description:** "As a user, I want to easily contact SeoAgency through a Contact Us page that includes a form with fields for my name, email, phone, and message, ensuring that my inquiries are recorded in the database for efficient response management."
- **Acceptance Criteria:**
  - The Contact Us page features a form that captures the user's name, email, phone number, and a message.
  - Each entry in the form is validated to ensure the data is in the correct format before submission.
  - Upon submission, the user's data is securely saved to a database, ensuring that the information can be accessed by customer service for follow-up.

#### 3. Services Interaction (SHOULD)

- **Name:** EnhancedServicesInteraction
- **Title:** Enhance interaction with services to improve user engagement and simplify administration
- **Description:** "As a user, I want to easily understand and interact with the services offered, including the ability to contact directly and submit requests. As an administrator, I want to effortlessly add, edit, and delete services directly from the website interface without accessing the admin panel. As a site owner, I aim to convert visitors into clients by utilizing an efficient contact form linked with each service."
- **Acceptance Criteria:**
  - **User Experience:**
    1. Users can view detailed descriptions of each service on the main services page.
    2. Each service includes a 'Contact Us' button that leads to a pre-filled contact form or provides direct contact details.
    3. Upon clicking the contact button, users can fill out and submit a form to inquire or request the service.
  - **Administrator Experience:**
    1. Administrators can add, edit, and delete service listings through a simplified interface accessible directly from the website, not just the admin panel.
    2. Changes made by administrators are reflected in real-time on the website.

### Epic 3: Website Administration

#### 1. Admin Create Service (SHOULD)

- **Name:** AdminCreateService
- **Title:** Allow admins to add new services directly from the website interface
- **Description:** "As an admin, I want to add new services to the website directly through a user-friendly interface on the main site so that users can see our latest offerings without my having to access the admin panel."
- **Acceptance Criteria:**
  1. Admins can access the service addition form directly on the website through a secure interface.
  2. New services are visible on the website upon creation.
  3. The process is secured and only accessible by users with admin rights.

#### 2. Admin Update Service (SHOULD)

- **Name:** AdminUpdateService
- **Title:** Allow admins to update existing services directly from the website interface
- **Description:** "As an admin, I want to be able to update service details directly on the website to ensure all service offerings are current and accurate, without needing to access the admin panel."
- **Acceptance Criteria:**
  1. Admins can access an update interface for each service on the website through a secure mechanism.
  2. Changes are immediately reflected on the service pages to ensure accurate and up-to-date information.
  3. This functionality is safeguarded and only available to users with administrative privileges.

#### 3. Admin Delete Service (COULD)

- **Name:** AdminDeleteService
- **Title:** Enable admins to delete services directly from the website interface
- **Description:** "As an admin, I need the ability to remove outdated or unnecessary services from the website directly using an interface accessible outside the admin panel to maintain a clean and relevant service offering."
- **Acceptance Criteria:**
  1. Admins can access a delete option for each service listed directly on the website.
  2. A confirmation process is required to prevent accidental deletions.
  3. Deleted services are immediately removed from the public-facing site.

### Epic 4: Subscription Management

#### 1. Create Subscription (MUST)

- **Name:** CreateSubscription
- **Title:** Enable users to initiate a new subscription
- **Description:** "As a user, I want to subscribe to the website's services so that I can enjoy SEO features."
- **Acceptance Criteria:**
  1. Users can access the subscription form from the price page.
  2. The form captures necessary information and payment details.

#### 2. Delete Subscription (MUST)

- **Name:** DeleteSubscription
- **Title:** Allow users to cancel their subscription
- **Description:** "As a user, I want to cancel my subscription so that I am not billed in the future."
- **Acceptance Criteria:**
  1. Users can easily find the cancel subscription option in their account settings.

#### 3. Subscription Status (SHOULD)

- **Name:** SubscriptionStatus
- **Title:** Provide users with their current subscription status
- **Description:** "As a user, I want to see my current subscription status so that I know the details of my subscription."
- **Acceptance Criteria:**
  1. Users can view their subscription status on their account settings page.

#### 4. Newsletter Subscription (SHOULD)

- **Name:** NewsletterSubscription
- **Title:** Offer a newsletter subscription to users
- **Description:** "As a user, I can subscribe to a newsletter so that I can stay informed about the latest news, offers, and updates from the restaurant."
- **Acceptance Criteria:**
  1. Users can subscribe using their email through a form on the homepage.
  2. Subscribers receive a confirmation email upon successful subscription.

### Epic 5: Site Stability and Performance

#### 1. Testing (SHOULD)

- **Name:** SiteTesting
- **Title:** Ensure site stability through testing
- **Description:** "As a website owner, I want my site to operate stably so that the user experience is uninterrupted and fluid."
- **Acceptance Criteria:**
  1. Manual testing is conducted on all major site features.
  2. Automated testing covers critical pathways and user interactions.

### Epic 6: Website Setup and Deployment

#### 1. Setup and Deploy (MUST)

- **Name:** SetupAndDeploy
- **Title:** Setup and deploy the restaurant website
- **Description:** "As a site owner, I want to create an agency website to enhance user convenience and grow up my business."
- **Acceptance Criteria:**
  1. The website is published on a reliable platform like Heroku.
  2. The database is connected and accessible, ensuring smooth site operation.

### Epic 7: Customer Engagement and Feedback

#### 1. Collect Feedback (COULD)

- **Name:** CollectFeedback
- **Title:** Collect user feedback through a form
- **Description:** "As a website owner, I can collect feedback directly from users so that I can understand their needs and improve the website."
- **Acceptance Criteria:**
  1. A feedback form is available on the website.
  2. Users receive a thank-you message after submitting feedback.

## UX/UI Design

### Using a ThemeForest Bootstrap5 Template for the SEOAGENCY project

For the development SEO agency website, I opted to utilize a pre-designed template from ThemeForest, created by the author thecodegrammer. This decision was strategically made to streamline the development process and focus efforts where they were most needed.

### Reasons for Choosing a Pre-Designed Template

#### 1. **Efficiency in Development**

- **Time Savings:** By using a ready-made template, I significantly reduced the time required for design and layout considerations. This allowed me to launch the project faster than if I had started from scratch.
- **Cost Efficiency:** Pre-designed templates also offer a cost advantage. The reduced development time translates into cost savings, which is crucial for managing the project budget effectively.

#### 2. **Focus on Essential Functionalities**

- **Core Features Prioritization:** With the design elements already in place, I was able to concentrate on integrating and refining the core functionalities that are critical for the project’s success. This focus ensured that I could deliver a robust platform that meets the specific needs of my users.
- **Quality Assurance:** Leveraging a well-constructed template allowed me to maintain high standards of quality for the website’s aesthetics and functionality, ensuring a professional look and feel that aligns with modern web standards.

#### 3. **Customization to Fit Project Needs**

- **Tailored Solutions:** Although the template provided a strong foundation, all pages and elements borrowed from the template were extensively customized to align with my specific project objectives and functions. This customization ensured that every aspect of the template was molded to support the unique features and workflows of my digital agency.
- **Branding Consistency:** Customizing the template also allowed me to seamlessly integrate my brand's visual identity and messaging, providing a consistent user experience that reflects my brand’s values and vision.

The decision to utilize a template from ThemeForest authored by thecodegrammer was instrumental in allowing me to dedicate more resources to critical aspects of the project, such as feature integration, user experience enhancements, and strategic deployment. The template not only provided a high-quality visual framework but also supported extensive customization to ensure that the final product truly represented my digital agency's innovative spirit and operational needs.
