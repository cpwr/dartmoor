import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
import 'package:frontend/constants.dart';
import 'package:frontend/screens/main/main_screen.dart';

import 'components/home_banner.dart';


class ContactsScreen extends StatelessWidget {
  const ContactsScreen({Key? key}) : super(key: key);

  static const String route = '/contacts';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Contacts'),
      ),
      body: Center(
        child: Container(
          child: Row(
            children: [
              ElevatedButton(
                child: const Text('Go back!'),
                onPressed: () {
                  // Navigate back to the first screen by popping the current route
                  // off the stack.
                  Navigator.pop(context);
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}