"""Tests for UnifiedStorageClient."""

import pytest
from pathlib import Path
from shared_modules.storage import UnifiedStorageClient


class TestUnifiedStorageClient:
    """Test suite for UnifiedStorageClient."""
    
    def test_local_backend_init(self, tmp_path):
        """Test initialization with local backend."""
        client = UnifiedStorageClient(backend="local", base_path=str(tmp_path))
        assert client.backend == "local"
    
    def test_upload_and_download_local(self, tmp_path):
        """Test upload and download with local backend."""
        # Create test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello, World!")
        
        # Initialize client
        storage_path = tmp_path / "storage"
        client = UnifiedStorageClient(backend="local", base_path=str(storage_path))
        
        # Upload
        result = client.upload_file(str(test_file), "uploads/test.txt")
        assert Path(result).exists()
        
        # Download
        download_path = tmp_path / "downloaded.txt"
        client.download_file("uploads/test.txt", str(download_path))
        assert download_path.read_text() == "Hello, World!"
    
    def test_list_objects_local(self, tmp_path):
        """Test listing objects with local backend."""
        storage_path = tmp_path / "storage"
        client = UnifiedStorageClient(backend="local", base_path=str(storage_path))
        
        # Create test files
        test_file = tmp_path / "test.txt"
        test_file.write_text("test")
        
        client.upload_file(str(test_file), "folder1/file1.txt")
        client.upload_file(str(test_file), "folder1/file2.txt")
        client.upload_file(str(test_file), "folder2/file3.txt")
        
        # List all
        all_files = client.list_objects()
        assert len(all_files) == 3
        
        # List with prefix
        folder1_files = client.list_objects("folder1")
        assert len(folder1_files) == 2
    
    def test_delete_object_local(self, tmp_path):
        """Test deleting objects with local backend."""
        storage_path = tmp_path / "storage"
        client = UnifiedStorageClient(backend="local", base_path=str(storage_path))
        
        # Create and upload file
        test_file = tmp_path / "test.txt"
        test_file.write_text("test")
        client.upload_file(str(test_file), "test.txt")
        
        # Verify exists
        assert client.object_exists("test.txt")
        
        # Delete
        assert client.delete_object("test.txt")
        assert not client.object_exists("test.txt")
    
    def test_unsupported_backend(self):
        """Test initialization with unsupported backend."""
        with pytest.raises(ValueError, match="Unsupported backend"):
            UnifiedStorageClient(backend="unsupported")
