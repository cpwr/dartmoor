import 'package:flutter/material.dart';
import 'package:frontend/screens/home/home_screen.dart';
import 'package:frontend/screens/main/main_screen.dart';
import 'package:google_fonts/google_fonts.dart';

import 'constants.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Практический психолог - Оксана Дегтяренко',
      // we are using dark theme and we modify it as our need
      theme: ThemeData.dark().copyWith(
        primaryColor: primaryColor,
        scaffoldBackgroundColor: bgColor,
        canvasColor: bgColor,
        textTheme: GoogleFonts.poppinsTextTheme(Theme.of(context).textTheme)
            .apply(bodyColor: Colors.white)
            .copyWith(
              bodyText1: TextStyle(color: bodyTextColor),
              bodyText2: TextStyle(color: bodyTextColor),
            ),
      ),
      initialRoute: '/',
      routes: {
        '/': (BuildContext context) => const HomeScreen(),
        '/about': (BuildContext context) => Scaffold(
              appBar: AppBar(
                title: const Text('About Route'),
              ),
            ),
        // '/profile': (BuildContext context) => ProfileScreen(),
      },
    );
  }
}
