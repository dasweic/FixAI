import '../../features/student/presentation/my_complaints_screen.dart';
import 'package:go_router/go_router.dart';
import '../../features/student/presentation/ai_review_screen.dart';
import '../../features/auth/presentation/splash_screen.dart';
import '../../features/auth/presentation/login_screen.dart';
import '../../features/student/presentation/raise_complaint_screen.dart';
import '../../features/student/presentation/complaint_details_screen.dart';
import '../../features/student/presentation/notifications_screen.dart'; 
import '../../features/student/presentation/profile_screen.dart';
import '../../features/student/presentation/student_shell_screen.dart';
import '../../features/admin/presentation/dashboard_screen.dart';
import '../../features/admin/presentation/complaint_list_screen.dart'; 
import '../../features/admin/presentation/admin_complaint_details_screen.dart'; 
import '../../features/admin/presentation/status_update_screen.dart';


class AppRouter {
  static final router = GoRouter(
    initialLocation: '/',
    routes: [

      GoRoute( 
        path: '/my-complaints', 
        builder: (context, state) => const MyComplaintsScreen(), 
      ),
      GoRoute(
        path: '/',
        builder: (context, state) => const SplashScreen(),
      ),

      GoRoute(
        path: '/login',
        builder: (context, state) => const LoginScreen(),
      ),

      GoRoute(
        path: '/student-home',
        builder: (context, state) => const StudentShellScreen(),
      ),

      GoRoute( 
        path: '/ai-review', 
        builder: (context, state) => const AIReviewScreen(), 
      ),

      GoRoute( 
        path: '/raise-complaint', 
        builder: (context, state) => const RaiseComplaintScreen(), 
      ),

      GoRoute( 
        path: '/complaint-details', 
        builder: (context, state) => const ComplaintDetailsScreen(), 
      ),

      GoRoute( 
        path: '/notifications', 
        builder: (context, state) => const NotificationsScreen(), 
      ), 

      GoRoute( 
        path: '/profile', 
        builder: (context, state) => const ProfileScreen(), 
      ), 

      GoRoute( 
        path: '/student-home', 
        builder: (context, state) => const StudentShellScreen(), 
      ),  

      GoRoute( 
        path: '/admin-dashboard', 
        builder: (context, state) => const AdminDashboardScreen(), 
      ),

      GoRoute(
        path: '/admin-complaints', 
        builder: (context, state) => const AdminComplaintListScreen(), 
      ), 
      
      GoRoute( 
        path: '/admin-complaint-details', 
        builder: (context, state) => const AdminComplaintDetailsScreen(), 
      ), 
      
      GoRoute( 
        path: '/status-update', 
        builder: (context, state) => const StatusUpdateScreen(), 
      ),
    ],
  );
}