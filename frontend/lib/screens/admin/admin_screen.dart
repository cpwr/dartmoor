import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:frontend/constants.dart';

class AdminMainScreen extends StatelessWidget {
  const AdminMainScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Admin'),
      ),
      body: SafeArea(
        child: Row(
          children: [
            Expanded(
              flex: 2,
              child: Column(
                children: [
                  DrawerHeader(child: 
                    Image.asset("assets/images/oksana.jpg")
                  ),
                  ListTile(
                    leading: SvgPicture.asset(
                      "assets/icons/settings.svg",
                      color: Colors.black,
                      height: 16,
                    ),
                    title: Text(
                      "Dashboard",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontWeight: FontWeight.w200,
                        height: 1.5,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            SizedBox(width: defaultPadding),
            Expanded(
              flex: 10,
              child: Container(
                color: Colors.white,
              ),
            ),
          ],
        ),
      ),
    );
  }
}