import 'package:go_router/go_router.dart';
import 'package:flutter/material.dart';

class ComplaintDetailsScreen extends StatelessWidget {
  const ComplaintDetailsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Complaint Details'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text(
            'Fan not working',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),

          const SizedBox(height: 12),

          Row(
            children: const [
              Chip(label: Text('Pending')),
              SizedBox(width: 8),
              Chip(label: Text('Electrical')),
            ],
          ),

          const SizedBox(height: 20),

          const Text(
            'Description',
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),

          const SizedBox(height: 8),

          const Text(
            'The ceiling fan in room H-204 is not working since yesterday. '
            'Please resolve the issue as soon as possible.',
          ),

          const SizedBox(height: 24),

          const Text(
            'Assigned Staff',
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),

          const SizedBox(height: 8),

          ListTile(
            onTap: () { 
              context.push('/complaint-details'); 
            },
            leading: CircleAvatar(child: Icon(Icons.person)),
            title: Text('Ramesh Kumar'),
            subtitle: Text('Electrical Department'),
          ),

          const SizedBox(height: 24),

          const Text(
            'Timeline',
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),

          const SizedBox(height: 12),

          _timelineTile(
            title: 'Complaint Submitted',
            subtitle: 'Today, 10:30 AM',
            icon: Icons.check_circle,
          ),

          _timelineTile(
            title: 'AI Review Completed',
            subtitle: 'Today, 10:31 AM',
            icon: Icons.smart_toy,
          ),

          _timelineTile(
            title: 'Assigned to Staff',
            subtitle: 'Today, 10:45 AM',
            icon: Icons.assignment_ind,
          ),
        ],
      ),
    );
  }

  static Widget _timelineTile({
    required String title,
    required String subtitle,
    required IconData icon,
  }) {
    return ListTile(
      leading: CircleAvatar(child: Icon(icon)),
      title: Text(title),
      subtitle: Text(subtitle),
    );
  }
}