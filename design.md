# User Story
```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.
```

# Nouns
user, username, email, post, title, content, views

# Column Table
| Record                | Properties                 |
| --------------------- | -------------------------- |
| users                 | username, email_address    |
| posts                 | title, content, view_count |

# Column Types

```
users:
    id: SERIAL
    username: text
    email_address: text

posts:
    id: SERIAL
    title: text
    content: text
    view_count: int
```

Can a user have multiple posts? YES\
Can a post have multiple users? NO\

-> Therefore,\
-> A user has many posts\
-> A post belogs to a user\

-> Therefore, the foreign key is on the posts table.