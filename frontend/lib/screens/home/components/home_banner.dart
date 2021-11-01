import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';

import '../../../constants.dart';

class HomeBanner extends StatelessWidget {
  const HomeBanner({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: 3,
      child: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset(
            "assets/images/background.jpg",
            fit: BoxFit.cover,
          ),
          Container(color: darkColor.withOpacity(0.66)),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: defaultPadding),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "Добро пожаловать на страницу психолога Оксаны Дегтяренко!",
                  style: Theme.of(context).textTheme.headline4!.copyWith(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                ),
                MyBuildAnimatedText(),
                SizedBox(height: defaultPadding),
                ElevatedButton(
                  onPressed: () {},
                  style: TextButton.styleFrom(
                    padding: EdgeInsets.symmetric(
                        horizontal: defaultPadding * 2,
                        vertical: defaultPadding),
                    backgroundColor: primaryColor,
                  ),
                  child: Text(
                    "Записаться на приём",
                    style: TextStyle(color: darkColor),
                  ),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }
}

class MyBuildAnimatedText extends StatelessWidget {
  const MyBuildAnimatedText({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return DefaultTextStyle(
      // it applies same style to all the widgets under it
      style: Theme.of(context).textTheme.subtitle1!,
      child: Row(
        children: [
          FlutterCodedText(),
          SizedBox(width: defaultPadding / 2),
          Text("Вместе мы можем "),
          AnimatedTextKit(
            animatedTexts: [
              TyperAnimatedText(
                "поговорить.",
                speed: Duration(milliseconds: 60),
              ),
              TyperAnimatedText(
                "порисовать.",
                speed: Duration(milliseconds: 60),
              ),
              TyperAnimatedText(
                "подумать.",
                speed: Duration(milliseconds: 60),
              ),
            ],
          ),
          SizedBox(width: defaultPadding / 2),
          FlutterCodedText(),
        ],
      ),
    );
  }
}

class FlutterCodedText extends StatelessWidget {
  const FlutterCodedText({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text.rich(
      TextSpan(
        text: "<",
        children: [
          TextSpan(
            text: "Важно!",
            style: TextStyle(color: primaryColor),
          ),
          TextSpan(text: ">"),
        ],
      ),
    );
  }
}
