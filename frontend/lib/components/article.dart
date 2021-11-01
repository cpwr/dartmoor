import 'package:flutter/material.dart';
import 'package:frontend/constants.dart';

class Article extends StatelessWidget {
  const Article({
    Key? key,
    required this.title,
    required this.description
  }) : super(key: key);

  final String title;
  final String description;

  @override
  Widget build(BuildContext context) {
    return Container( // grey box
      child: Center(
        child: Container( // red box
          child: TextButton(
            style: TextButton.styleFrom(
              textStyle: const TextStyle(fontSize: 20),
            ),
            child: Text(
              title,
              style: TextStyle(
                color: primaryColor,
              ),
            ),
            onPressed: () {
              // Navigate back to the first screen by popping the current route
              // off the stack.
              Navigator.of(context).pushNamed('/contacts/');
            },
          ),
          decoration: BoxDecoration(
            color: Colors.red[400],
          ),
          padding: EdgeInsets.all(20),
        ),
      ),
      width: 320,
      height: 240,
      color: Colors.grey[300],
    );
  }
}

class ArticleTitle extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    throw UnimplementedError();
  }
  
}

