# Instructor Checklist

## General Tips

- The curriculum on GitHub is a good guide to the language features and sorts of practical development skills that students need to learn in this course, but it is not an exhaustive list of the higher level concepts that students also need to at least be introduced to during their time here. The following is an incomplete list of things you should make sure to also cover:
  * IDEs, tooling, debugging, and other developer tools
  * Design Patterns (publish/subscribe, more in depth on MVC, etc.)
  * Software engineering principles (modularity, composeability, etc.)
  * Type systems (such as the trend in web right now to add static types to javascript)
  * Paradigms (actually go more in depth on FP and OOP)
  * Architecture (layers, dependency inversion, etc.)
  * Testing (unit vs integration vs system test, TDD, etc.)
  * Agile and Scrum
- Don't just teach off the docs, have a lesson plan so that you cover everything you need and want to cover. Make your plan comprehensive, but flexible. You will need to adjust it for every unique class.
- Try to teach in varying ways that utilize multiple learning styles. Demo lots of code, both visually and out loud. Include students in lectures, solicit input, and ask them questions.
- Do occasional pair/group/mob exercises, but make sure the vast majority of class work is individual.
- Make sure you have (or can think up) a limitless amount of challenges to keep advanced students busy, especially if part of the class is struggling and you have to slow the class's pace.
- Especially these days, pay attention to your students' mental health. This program is mentally and emotionally exhausting for the students in the best situations, but these days there's a lot on peoples' minds. Be encouraging and understanding.
- Encourage students to chat, banter, post memes, etc in class and on Slack. It helps establish class culture and a sense of belonging.

## Scheduling

The day class is 14 weeks long, and the night class is 16 weeks long. This means that day classes have 70 sessions and night classes have 80 sessions. To facilitate holidays, instructor sick/personal days, flexibility, etc, classes are scheduled for one additional week. This means the day class has 15 weeks to fit in 70 sessions and the night class has 17 weeks to fit in 80 sessions. Our relationship with the VA means there are some strict rules we have to follow so that students recieve their full housing allowance and the Code Guild stays compliant with federal rules.

Classes need to end with their graduation date on the last day of the 15th/17th week of class. Classes cannot take no breaks and end early. It is up to instructors to schedule days off so that the class does not end early. Similarly, if an instructor needs to take extra sick/personal days, they need to find a substitute teacher so that the last day of class does not get pushed back. With this in mind, when using your five discretional days you have to cancel class during a cohort, don't use them all at once so that if an emergency happens and you have to add a couple more days, you don't go over.

During a bootcamp, class must be offered at least one day in any seven calendar days. Class can not be cancelled or scheduled off for planed dates such as holidays/weekends more than six contiguous days in a row. The VA does not allow us to take an entire week off during a bootcamp, and if this happens, veterans have to pay back that week's housing allowance.

## Teaching Tools, PDX Code Guild Style

### Slack

We use Slack for quick communication between students and staff. You will need to create a separate Slack channel for each class. This should be labelled with the course name and start end/dates in either the name or the description of the channel. This is what you'll use to share things with students, notify them of last minute changes of plans, chat with students to help them or answer questions, etc.

Keep in mind that Slack is ***ephemeral***. We're on the free Slack plan, so only about 2.5 weeks of past messages are accessible. Even if we were on a paid plan, Slack does not work well as a communications archive or a file sharing system. Anything you want to share with students as a reference should go on GitHub so it is easy to find later. Any docs you want as reference or to share with staff should be on Google Drive. Any communication with students/staff you want a written copy of should be sent via email. Slack is a chat system -- only use it as a chat system.

### Github

Every class has its own GitHub repository with class information, lecture notes, labs, and solutions. This is also where students upload their own labs for both grading and practice.

To create this repo, start with the files (not the repo itself) from either this repository or a finished class and upload as a fresh repo. We usually name the repos "class_whatever" to shorten the repo name and promote class culture, but make sure that the repo has notes in the description AND readme with the official name of the class, such as "Python Full-Stack Day Class 02/07/2020".

Start with just the "0 Intro" and "1 Python" folders and upload the different units as you go. Also create a "code" folder where students can create a folder where they will post all their labs. Creating this folder and committing is a great first day of class activity to practice Git and the command line. By having students commit to a common repo, you can grade easily, and keep an eye on their code and progress to catch early if people are falling behind or not getting their work done.

Make sure you think about GitHub permissions. If you give students write access to the class repo, make sure you have a local copy and make sure you know how to undo anything a student might do. This is very rare, but occasionally a student merges something they shouldn't and messes up the timeline. An alternative is to only allow read access to the repository, and have students submit pull requests with finished labs. This makes it easier to administer the repo, but has two major pitfalls: you will have to teach the students about branching/merging/pull requests at the start of the class (and this will be very difficult for many students to grasp the first week), and it will make it harder for you to keep track of student progress.

In the readme for your repo, include class information, dates, lists of assignments, and external resources students might find handy. You can find examples in any existing class repo.

### Zoom

You will hold your actual class sessions using Zoom. This is the closest we can get to being "in person" without actually being in person. Here are some tips for Zoom:

- Put a password on your meeting for security.
- Avoid using in-meeting chat for important things. It's even more ephemeral and notifications/messages are easy to miss.
- As the meeting host, you can mute/unmute/kick out/etc people if trouble arises (or if someone just forgets to turn off their mic).
- Test your webcam and mic settings before you start the meeting, and give yourself extra time the first day.
- As a Zoom admin account and meeting host, you can change any settings to your liking. Remember there are a lot of customizations and available by logging in to [Zoom's website](https://zoom.us/profile).
- Use screen sharing for lectures. Unless there's something on your screen you absolutely need to have on the screen but not seen by students, it's best to share a whole desktop and minimize or move another desktop anything you don't want to broadcast. Sharing one app at a time is really clunky.
- You can also screen share a "whiteboard" that can be drawn on. This is great for using just like a real whiteboard. It works best if you have a touchscreen or an iPad you can run it on.
- The whiteboard-style drawing and annotation tools can be used to mark up a screen share live.
- There is a remote control option. I don't recommend using it. I don't want students controlling my computer, and I want students to always have to go through the motions of typing code and making changes themselves, even if following instructions.
- During worktime, use breakout rooms to meet with students individually as you would in a classroom setting. Only the host can edit breakout rooms, so you'll have to set themn up and put TAs/students in them. It's best to open several (4-6) breakout rooms at one time with manual assigning, that way you can add students to new breakout rooms as necessary. Breakout rooms are a bit of a clunky feature in Zoom at the moment and don't always seem to work intuitively, so plan on it being annoying until you've had some practice.
- Tell students to keep themselves muted by default unless they are talking.
- On the other hand, make sure students keep their cameras on, except during breaks. This is very important for several reasons: it counts as "in-person" attendance, it discourages students slacking and promotes a professional academic enviroment, it emulates the in person experience and provides familiarity for students, and it promotes class community, cohesiveness, and culture. Requiring cameras on is an important step to create a classroom enviroment that emulates "real life" as much as possible.
- You can schedule reoccuring meetings in Zoom with set start and end dates.

### Google Drive

Staff files and class records should be kept on Google Drive. This includes attendance and progress gradesheets. Make sure you share class records such as attendance with Sheri and Lynn, as well as TAs if you want them to be able to access them. There is an "Instructor Documents" folder with templates of attendance sheets, progress reports, etc.

## Things To Do

### The Week Before

- [Create attendance sheet](https://docs.google.com/spreadsheets/d/1SEPHXpAQda5-P2B8gHPz1rlVAD7452LhQVrcUJqsId4/edit?usp=sharing)
- Create Github repo
- Create Slack channel
- [Send welcome email to students with information on how to get started with remote apps](Welcome%20Email.md)

### Day 1

- Intro to Zoom
- Instructor personal intro
- Student intros:
  1. Name
  2. Personal and/or tech background
  3. Why are you here?
  4. What do you want to get out of this course?
- Code of conduct/inclusion
- Go over objectives
- Go over curriculum
- Go over rules and logistics
- Instructor teaching style
- Add students to attendance sheets
- Add students to Slack channel
- Add students to Github + repo
- Set up students' computers with command line/IDE/Python/Git/etc

### Ongoing

- If there's a problem with a student (and/or you have to meet with them) send a follow up email to them and Sheri so that there's a record

### Every Week

- Update grading sheet
- Make sure you/a TA touches base at LEAST once a week with each student. This doesn't have to be an in depth conference, but it is way too easy for remote students to fall through the cracks without constant progress check-ins.

### 25%

- Send students + Sheri individual progress reports

### 45%

- Send students + Sheri individual progress reports

### 75% or when beginning capstone section

- Send students + Sheri individual progress reports

### Last Week

- Send Sheri list of graduating students and name spellings
- Make catch-up plans for students not on track
- Announce graduation on Slack

### Last Day

- Introduce students and capstones
- Make sure students know next steps
- Distribute certificates
