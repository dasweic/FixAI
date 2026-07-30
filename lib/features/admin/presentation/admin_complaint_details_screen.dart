import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class AdminComplaintDetailsScreen extends StatelessWidget {
  const AdminComplaintDetailsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Complaint Details'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Fan not working',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),

            const SizedBox(height: 12),

            const Chip(label: Text('Pending')),

            const SizedBox(height: 20),

            const Text(
              'Student: Rahul Sharma',
              style: TextStyle(fontSize: 16),
            ),

            const SizedBox(height: 8),

            const Text(
              'Room: H-204',
              style: TextStyle(fontSize: 16),
            ),

            const SizedBox(height: 20),

            const Text(
              'The ceiling fan is not working since yesterday.',
            ),

            const Spacer(),

            SizedBox(
              width: double.infinity,
              height: 52,
              child: FilledButton(
                onPressed: () {
                  context.push('/status-update');
                },
                child: const Text('Update Status'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}