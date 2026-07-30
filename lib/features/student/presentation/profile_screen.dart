import 'package:flutter/material.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  bool isDark = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Profile'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            const SizedBox(height: 24),

            const CircleAvatar(
              radius: 40,
              child: Icon(Icons.person, size: 40),
            ),

            const SizedBox(height: 16),

            const Text(
              'Student Name',
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 8),

            const Text('student@fixai.com'),

            const SizedBox(height: 24),

            SwitchListTile(
              title: const Text('Dark Mode'),
              secondary: const Icon(Icons.dark_mode),
              value: isDark,
              onChanged: (value) {
                setState(() {
                  isDark = value;
                });

                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(
                      value
                          ? 'Dark mode enabled (demo)'
                          : 'Light mode enabled (demo)',
                    ),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}