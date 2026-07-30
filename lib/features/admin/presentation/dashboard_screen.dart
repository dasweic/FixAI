import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class AdminDashboardScreen extends StatelessWidget {
  const AdminDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final cards = [
      ('Total', '120', Icons.dashboard),
      ('Pending', '32', Icons.pending_actions),
      ('In Progress', '48', Icons.build),
      ('Resolved', '40', Icons.check_circle),
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Admin Dashboard'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: GridView.builder(
          itemCount: cards.length,
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            crossAxisSpacing: 12,
            mainAxisSpacing: 12,
            childAspectRatio: 1.2,
          ),
          itemBuilder: (context, index) {
            final item = cards[index];

            return InkWell(
  borderRadius: BorderRadius.circular(16),
  onTap: () {
    context.go('/admin-complaints');
  },
  child: Card(
    elevation: 2,
    child: Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(item.$3, size: 36),
          const SizedBox(height: 12),
          Text(
            item.$2,
            style: const TextStyle(
              fontSize: 28,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 6),
          Text(item.$1),
        ],
      ),
    ),
  ),
);
          },
        ),
      ),
    );
  }
}