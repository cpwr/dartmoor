import 'package:flutter/material.dart';

class MyInfo extends StatelessWidget {
  const MyInfo({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: 1.23,
      child: Container(
        color: Colors.amber,
        child: Column(
          children: [
            Spacer(flex: 2),
            CircleAvatar(
              radius: 75,
              backgroundImage: AssetImage("assets/images/oksana.jpg"),
            ),
            Spacer(),
            Text(
              "Оксана Дегтяренко",
              style: Theme.of(context).textTheme.subtitle1,
            ),
            Text(
              "Практический психолог",
              textAlign: TextAlign.center,
              style: TextStyle(
                fontWeight: FontWeight.w200,
                height: 3.5,
              ),
            ),
            Spacer(flex: 2),
          ],
        ),
      ),
    );
  }
}
