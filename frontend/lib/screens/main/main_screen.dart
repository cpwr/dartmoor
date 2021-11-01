import 'dart:html';

import 'package:flutter/material.dart';
import 'package:frontend/components/article.dart';
import 'package:frontend/constants.dart';

import 'components/side_menu.dart';
import 'components/area_info_text.dart';

class MainScreen extends StatefulWidget {
  final String? title;

  MainScreen({Key? key, this.title}) : super(key: key);

  @override
  _MainScreenState createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _selectedDestination = 0;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final textTheme = theme.textTheme;

    return Scaffold(
      resizeToAvoidBottomInset: true,
      appBar: AppBar(
        title: Text(""),
      ),
      drawer: Drawer(
        child: ListView(
          // Important: Remove any padding from the ListView.
          padding: EdgeInsets.zero,
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Text(
                'Header',
                style: textTheme.headline6,
              ),
            ),
            Divider(
              height: 1,
              thickness: 1,
            ),
            ListTile(
              leading: Icon(Icons.favorite),
              title: Text('Item 1'),
              selected: _selectedDestination == 0,
              onTap: () => selectDestination(0),
            ),
            ListTile(
              leading: Icon(Icons.delete),
              title: Text('Item 2'),
              selected: _selectedDestination == 1,
              onTap: () => selectDestination(1),
            ),
            ListTile(
              leading: Icon(Icons.label),
              title: Text('Item 3'),
              selected: _selectedDestination == 2,
              onTap: () => selectDestination(2),
            ),
            Divider(
              height: 1,
              thickness: 1,
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Text(
                'Label',
              ),
            ),
            ListTile(
              leading: Icon(Icons.bookmark),
              title: Text('Item A'),
              selected: _selectedDestination == 3,
              onTap: () => selectDestination(3),
            ),
          ],
        ),
      ),
      body: Center(
        child: Container(
          constraints: BoxConstraints(maxWidth: maxWidth),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Expanded(
                flex: 2,
                child: SideMenu(),
              ),
              SizedBox(width: defaultPadding),
              Expanded(
                flex: 7,
                child: ListView.separated(
                  controller: ScrollController(),
                  itemCount: 20,
                  padding: const EdgeInsets.all(20),
                  separatorBuilder: (BuildContext context, int index) => const Divider(
                    thickness: 2,
                  ),
                  itemBuilder: (BuildContext context, int index) {
                    return Card(
                      clipBehavior: Clip.antiAlias,
                      child: Column(
                        children: [
                          ListTile(
                            leading: Icon(Icons.arrow_drop_down_circle),
                            title: const Text('Card title 1'),
                            subtitle: Text(
                              'Secondary Text',
                              style: TextStyle(color: Colors.black.withOpacity(0.6)),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(16.0),
                            child: Text(
                              'Greyhound divisively hello coldly wonderfully marginally far upon excluding.',
                              style: TextStyle(color: Colors.black.withOpacity(0.6)),
                            ),
                          ),
                          ButtonBar(
                            alignment: MainAxisAlignment.start,
                            children: [
                              TextButton(
                                onPressed: () {
                                  // Perform some action
                                },
                                child: const Text('ACTION 1'),
                              ),
                              TextButton(
                                onPressed: () {
                                  // Perform some action
                                },
                                child: const Text('ACTION 2'),
                              ),
                            ],
                          ),
                          Image.asset('assets/card-sample-image.jpg'),
                        ],
                      )
                    );
                  }
                ),
              ),
              SizedBox(width: defaultPadding),
            ],
          ),
        ),
      ),
    );
  }

  void selectDestination(int index) {
    setState(() {
      _selectedDestination = index;
    });
  }
}
