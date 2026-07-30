import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class MyComplaintsScreen extends StatelessWidget {
  const MyComplaintsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final complaints = [
      {
        'title': 'Fan not working',
        'status': 'Pending',
      },
      {
        'title': 'Water leakage',
        'status': 'In Progress',
      },
      {
        'title': 'WiFi issue',
        'status': 'Resolved',
      },
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('My Complaints'),
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: complaints.length,
        itemBuilder: (context, index) {
          final complaint = complaints[index];

          return Card(
            margin: const EdgeInsets.only(bottom: 12),
            child:ListTile(
              onTap: () {
                context.push('/complaint-details');
              },
              leading: const CircleAvatar(
                child: Icon(Icons.report_problem),
              ),
              title: Text(complaint['title']!),
              subtitle: Text(complaint['status']!),
              trailing: Chip(
                label: Text(complaint['status']!),
              ),
            )
          );
        }
      )
    );
  }
}
