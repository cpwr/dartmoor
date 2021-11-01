import 'package:flutter/material.dart';
import 'package:frontend/screens/contacts/contacts_screen.dart';
import 'package:frontend/screens/main/main_screen.dart';
import 'package:frontend/screens/admin/admin_screen.dart';
import 'package:frontend/screens/login/login_screen.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:url_strategy/url_strategy.dart';
import 'package:frontend/models/Project.dart';

import 'constants.dart';

void main() {
  // Here we set the URL strategy for our web app.
  // It is safe to call this function when running on mobile or desktop as well.
  setPathUrlStrategy();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}): super(key: key);

  @override
  Widget build(BuildContext context) {
      List<Project> demo_projects = [
      Project(
        title: "Responsive Admin Panel or Dashboard - Flutter UI",
        description:
            "On Flutter V2.* web officially supported on a stable branch. Today I share an Admin panel or you can call it dashboard UI build with flutter. Now you can build your app dashboard using flutter. This dashboard contains almost everything that you need like a chart, table, nice small card for showing info.",
      ),
      Project(
        title: "E-Commerce Complate App - Flutter UI",
        description:
            "In the first part of our complete e-commerce app, we show you how you can create a nice clean onboarding screen for your e-commerce app that can run both Andriod and iOS devices because it builds with flutter. Then on the second episode, we build a Sign in, Forgot Password screen with a custom error indicator.",
      ),
      Project(
        title: "Outlook Email App Redesign - Flutter Fully Responsive Design UI",
        description:
            "We redesign the outlook app also make it responsive so that you can run it everywhere on your phone, tab, or web. In this flutter responsive video, we will show you the real power of flutter. Make mobile, web, and desktop app from a single codebase.",
      ),
      Project(
        title: "Chat/Messaging App Light and Dark Theme - Flutter UI",
        description:
            "Today we gonna build messing/chat app #ui using #flutter that runs both Android and iOS devices also has a dark and light theme. We create in total 4 screens all of that support both Dark Theme and Light Theme. At first, we design a welcome screen that contains an image with a tag line also has a skip button.",
      ),
      Project(
        title: "Welcome page, Login Page and Sign up page - Flutter UI",
        description:
            "In the first part of our complete e-commerce app, we show you how you can create a nice clean onboarding screen for your e-commerce app that can run both Andriod and iOS devices because it builds with flutter. Then on the second episode, we build a Sign in, Forgot Password screen with a custom error indicator.",
      ),
      Project(
        title: "Covid-19 App - Flutter UI",
        description:
            "We redesign the outlook app also make it responsive so that you can run it everywhere on your phone, tab, or web. In this flutter responsive video, we will show you the real power of flutter. Make mobile, web, and desktop app from a single codebase.",
      ),
    ];
    return MaterialApp(
      title: 'Практический психолог - Оксана Дегтяренко',
      theme: ThemeData.dark().copyWith(
        primaryColor: primaryColor,
        scaffoldBackgroundColor: bgColor,
        canvasColor: bgColor,
        textTheme:
          GoogleFonts.poppinsTextTheme(Theme.of(context).textTheme)
          .apply(bodyColor: Colors.white)
          .copyWith(
            bodyText1: const TextStyle(color: bodyTextColor),
            bodyText2: const TextStyle(color: bodyTextColor),
          ),
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => MainScreen(title: ""),
        '/contacts/': (context) => ContactsScreen(),
        '/admin/': (context) => AdminMainScreen(),
        // '/login/': (context) => LoginScreen(),
      },
    );
  }
}
